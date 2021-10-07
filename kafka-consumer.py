from kafka import KafkaConsumer
import time
import json

consumer = KafkaConsumer(
    "hepsiburada-kafka",
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = "latest",
    enable_auto_commit = True,
)


import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        database = "data-db",
        user = "postgres",
        password = "123456",
        port = "5432"
    )
    return conn


conn = get_conn()
cx = conn.cursor()
for msg in consumer:
    try:
        timex = msg.timestamp
        converted = json.loads(msg.value)
        product_id = converted.get("properties").get("productid")
        source = converted.get("context").get("source")
        user_id = converted.get("userid")
        print(timex,product_id,source,user_id)
        cx.execute("INSERT INTO product_views(user_id,product_id,source,timestamp) VALUES (%s,%s,%s,%s)",(user_id,product_id,source,timex))
        conn.commit()
    except Exception as e:
        print(e)




