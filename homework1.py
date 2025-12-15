
# # 5 ta masala
# -- select unit_price from products where unit_price>100
#
# -- select * from customers where country = 'USA'
#
# -- select * from products where product_name like 'a%' and unit_price>10 and unit_price<100
#
# -- select * from categories where category_name like '%b'
#
# -- select * from orders
# -- where extract(year from order_date) = 1997
# -- and extract(month FROM order_date)  between 01 and 06
# -- and shipped_date>required_date
#
# -- SELECT * FROM orders
# -- WHERE TO_CHAR(order_date, 'YYYY') = '1997'
#  -- AND TO_CHAR(order_date, 'MM') BETWEEN '01' AND '06'
#  -- AND shipped_date > required_date;

# CREATE TABLE categories (
#     category_id SERIAL PRIMARY KEY,
#     category_name VARCHAR(50)
# );
#
# INSERT INTO categories (category_name) VALUES
# ('Beverages'),
# ('Condiments'),
# ('Confections');

# CREATE TABLE products (
#     product_id SERIAL PRIMARY KEY,
#     product_name VARCHAR(50),
#     unit_price NUMERIC(10,2),
#     category_id INT REFERENCES categories(category_id)
# );
#
# INSERT INTO products (product_name, unit_price, category_id) VALUES
# ('Chai', 18.00, 1),
# ('Chang', 19.00, 1),
# ('Aniseed Syrup', 10.00, 2);

# CREATE TABLE suppliers (
#     supplier_id SERIAL PRIMARY KEY,
#     supplier_name VARCHAR(50),
#     country VARCHAR(50)
# );
# INSERT INTO suppliers (supplier_name, country) VALUES
# ('Exotic Liquids', 'UK'),
# ('New Orleans Cajun', 'USA'),
# ('Grandma Kelly', 'USA');

# CREATE TABLE orders (
#     order_id SERIAL PRIMARY KEY,
#     order_date DATE,
#     shipped_date DATE
# );
# INSERT INTO orders (order_date, shipped_date) VALUES
# ('2025-01-01','2025-01-03'),
# ('2025-02-15','2025-02-18'),
# ('2025-03-20','2025-03-25');

# CREATE TABLE order_details (
#     order_detail_id SERIAL PRIMARY KEY,
#     order_id INT REFERENCES orders(order_id),
#     product_id INT REFERENCES products(product_id),
#     quantity INT
# );
# INSERT INTO order_details (order_id, product_id, quantity) VALUES
# (1, 1, 5),
# (1, 2, 10),
# (2, 3, 7);

# INSERT INTO products (product_name, unit_price, category_id) VALUES
# ('Ikra', 25.00, 3);

# DELETE FROM products
# WHERE product_id = 2;

# ALTER TABLE products
# RENAME COLUMN unit_price TO price;
