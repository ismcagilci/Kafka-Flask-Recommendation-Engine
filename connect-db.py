import psycopg2

def get_cursor():
    conn = psycopg2.connect(
        host="localhost",
        database = "data-db",
        user = "postgres",
        password = "123456",
        port = "5432"
    )
    cx = conn.cursor()
    return cx

