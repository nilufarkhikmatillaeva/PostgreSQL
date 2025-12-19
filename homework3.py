# -- select p.product_name, s.company_name, o.order_date from products p
# -- inner join order_details od on p.product_id = od.product_id
# -- inner join orders o on od.order_id = o.order_id
# -- inner join suppliers s on p.supplier_id = s.supplier_id
# -- where to_char(o.order_date, 'yyyy-mm') = '1996-07'
#
# -- select c.company_name, e.first_name , c.city, e.city from customers c
# -- inner join orders o on o.customer_id = c.customer_id
# -- inner join employees e on e.employee_id = o.employee_id
# -- where e.city = c.city
#
# -- select p.product_name, c.company_name, sum(od.quantity), to_char(o.order_date, 'yyyy') from orders o
# -- inner join order_details od on od.order_id = o.order_id
# -- inner join products p on od.product_id = p.product_id
# -- inner join customers c on o.customer_id = c.customer_id
# -- group by to_char(o.order_date, 'yyyy'), p.product_name, c.company_name
#
# -- select p.product_name, count(o.order_id), to_char(o.order_date, 'YYYY_MM') from orders o
# -- inner join order_details od on o.order_id = od.order_id
# -- inner join products p on p.product_id = od.product_id
# -- where o.shipped_date>o.required_date
# -- group by p.product_name, to_char(o.order_date, 'YYYY_MM')
# -- order by to_char(o.order_date, 'YYYY_MM')

# select max(od.quantity), p.product_name from products p
# -- inner join order_details od on p.product_id = od.product_id
# -- group by product_name

