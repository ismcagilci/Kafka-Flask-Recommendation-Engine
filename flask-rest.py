from flask import Flask, request
app = Flask(__name__)

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
cnx = conn.cursor()


@app.route('/userviewInfo', methods=['POST','GET','DELETE'])
def user_views():
    if request.method == 'GET':
        get_user_id = request.form["user-id"]
        cnx.execute("select * from product_views WHERE user_id='{}' ORDER BY timestamp DESC LIMIT 10".format(get_user_id))
        new_list = []
        all_data = cnx.fetchall()
        new_dict = {}
        for data in all_data:
            new_list.append(data[1])
        new_dict['user-id'] = all_data[0][0]
        new_dict['products'] = new_list
        new_dict['type'] = "personalized"
        return new_dict
    if request.method == 'DELETE':
        get_user_id = request.form["user-id"]
        get_product_id = request.form["product-id"]
        cnx.execute("DELETE from product_views WHERE product_id='{}' and user_id = '{}' ".format(get_product_id,get_user_id))
        conn.commit()
        return "<p>Product was deleted succesfully!</p>"


@app.route('/bestSeller', methods=['GET'])
def best_seller():
    if request.method == "GET":
        get_user_id = request.form["user-id"]
        cnx.execute("select COUNT(product_id),product_id,category_id,user_id from (select product_views.product_id,products.category_id,user_id from product_views LEFT JOIN products ON product_views.product_id = products.product_id) AS deneme WHERE user_id = '{}' GROUP BY product_id,category_id,user_id ORDER BY COUNT(product_id) DESC LIMIT 3;".format(get_user_id))
        most_viewed_category = []
        all_data = cnx.fetchall()
        for data in all_data:
            most_viewed_category.append(data[2])
        best_seller_product = []
        for category in most_viewed_category:
            cnx.execute("select product_id,category_id,SUM(quantity) as sum_quantity from (select order_items.product_id,products.category_id,order_items.quantity from order_items LEFT JOIN products ON order_items.product_id = products.product_id LEFT JOIN orders ON order_items.order_id = orders.order_id ORDER BY quantity DESC) as deneme WHERE category_id = '{}' GROUP BY quantity,product_id,category_id ORDER BY sum_quantity DESC LIMIT 3".format(category))
            all_data = cnx.fetchall()
            for i in all_data:
                best_seller_product.append(i[0])
        new_dict = {}
        new_dict['user-id'] = get_user_id
        new_dict['products'] = best_seller_product
        new_dict['type'] = 'personalized'
        return new_dict








if __name__ == '__main__':
    app.run()