select * from order_items LEFT JOIN products ON order_items.product_id = products.product_id LEFT JOIN orders ON order_items.order_id = orders.order_id ORDER BY quantity ASC LIMIT 5;

CREATE TABLE product_views (
	user_id VARCHAR ( 50 ) PRIMARY KEY,
	product_id VARCHAR ( 50 ),
	context VARCHAR ( 50 ),
    timestamp VARCHAR ( 50 ),
);


select product_id,category_id,SUM(quantity) as sum_quantity from (select order_items.product_id,products.category_id,order_items.quantity from order_items LEFT JOIN products ON order_items.product_id = products.product_id LEFT JOIN orders ON order_items.order_id = orders.order_id ORDER BY quantity DESC) as deneme WHERE category_id = 'category-13' GROUP BY quantity,product_id,category_id ORDER BY sum_quantity DESC

