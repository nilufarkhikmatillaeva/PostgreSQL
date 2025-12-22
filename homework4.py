# -- SELECT
# --   e.country AS employee_country,
# --   COUNT(o.order_id) AS total_orders
# -- FROM employees e
# -- LEFT JOIN orders o
# --   ON o.employee_id = e.employee_id
# -- GROUP BY e.country
# -- ORDER BY total_orders DESC
#
# -- WITH cat1_sales AS (
# --   SELECT
# --     p.product_id,
# --     p.product_name,
# --     s.company_name AS supplier_company,
# --     MAX(od.unit_price) AS max_sold_price
# --   FROM products p
# --   JOIN suppliers s
# --     ON s.supplier_id = p.supplier_id
# --   JOIN order_details od
# --     ON od.product_id = p.product_id
# --   WHERE p.category_id = 1
# --   GROUP BY p.product_id, p.product_name, s.company_name
# -- ),
# -- top10 AS (
# --   SELECT *
# --   FROM cat1_sales
# --   ORDER BY max_sold_price DESC
# --   FETCH FIRST 10 ROWS ONLY       -- Oracle/PostgreSQL; MySQL: LIMIT 10; SQL Server: TOP 10
# -- )
# -- SELECT
# --   t.product_id,
# --   t.product_name,
# --   t.max_sold_price,
# --   t.supplier_company,
# --   c.customer_id,
# --   c.company_name AS customer_company
# -- FROM top10 t
# -- JOIN order_details od
# --   ON od.product_id = t.product_id
# -- JOIN orders o
# --   ON o.order_id = od.order_id
# -- JOIN customers c
# --   ON c.customer_id = o.customer_id
# -- GROUP BY
# --   t.product_id, t.product_name, t.max_sold_price, t.supplier_company,
# --   c.customer_id, c.company_name
# -- ORDER BY t.max_sold_price DESC, t.product_id, c.customer_id;
#
# -- WITH customer_orders AS (
# --   SELECT
# --     c.customer_id,
# --     c.company_name,
# --     c.city,
# --     COUNT(o.order_id) AS orders_count
# --   FROM customers c
# --   LEFT JOIN orders o
# --     ON o.customer_id = c.customer_id
# --   WHERE c.city = 'London'
# --   GROUP BY c.customer_id, c.company_name, c.city
# -- )
# -- SELECT COUNT(*) AS low_order_companies
# -- FROM customer_orders
# -- WHERE orders_count < 5;