# Kafka-Flask-Recommendation-Engine


### 1-Create Kafka Topic called hepsiburada-kafka
### 2-Get data from product.json and write to hepsiburada-kafka topic with python
### 3-Get writed data from topic,add timestamp value and load into the new table called product_views and this product_views table is on data-db database
### 4-Using product_views table, get last ten prouducts viewed and put these data to flask rest api

### 5-Example of last ten products viewed by used, you can reach this data from userviewInfo url
![lastviewed](https://user-images.githubusercontent.com/50598846/136380362-a31b9f2f-2b3c-4633-8bd7-21170a111171.png)

### 6-Example of deleted product
![deleted](https://user-images.githubusercontent.com/50598846/136380336-b880452f-8203-4f3a-b1b7-4fd095c78965.png)

### 7-Using all tables, i collected best seller products in all categories after that i recommend these products to user using their browsing history, you can reach these data from bestSeller url
![bestSeller](https://user-images.githubusercontent.com/50598846/136380293-c601c9bf-d221-4151-ba7d-6faf575a2ed0.png)
