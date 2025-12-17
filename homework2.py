# -- select customers.country, count(orders.order_id) from customers, orders
# -- where customers.customer_id = orders.customer_id
# -- group by customers.country;
#
# -- select customers.country, customers.customer_id,count(orders.order_id) from customers, orders
# -- where customers.customer_id = orders.customer_id
# -- and customers.country = 'USA'
# -- group by customers.customer_id;
#
# -- SELECT
# --     customers.country,
# --     COUNT(orders.order_id)
# -- FROM customers, orders
# -- WHERE customers.customer_id = orders.customer_id
# --   AND orders.shipped_date > orders.required_date
# -- GROUP BY customers.country
# -- HAVING COUNT(orders.order_id) > 2;
#
# -- SELECT
# --     employees.employee_id,
# --     EXTRACT(YEAR FROM orders.order_date),
# --     COUNT(orders.order_id)
# -- FROM employees, orders
# -- WHERE employees.employee_id = orders.employee_id
# --   AND employees.country = 'USA'
# -- GROUP BY employees.employee_id, EXTRACT(YEAR FROM orders.order_date);
#
# -- SELECT
# --     COUNT(order_details.order_id)
# -- FROM products, order_details
# -- WHERE products.product_id = order_details.product_id
# --   AND products.unit_price = (
# --       SELECT MIN(unit_price)
# --       FROM products
# --   );
#
# SELECT
#     suppliers.supplier_id,
#     COUNT(DISTINCT orders.order_id)
# FROM suppliers, products, order_details, orders
# WHERE suppliers.supplier_id = products.supplier_id
#   AND products.product_id = order_details.product_id
#   AND order_details.order_id = orders.order_id
# GROUP BY suppliers.supplier_id;