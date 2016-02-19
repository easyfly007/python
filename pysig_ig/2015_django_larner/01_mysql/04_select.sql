SELECT  [options] items
[INTO file_details]
FROM tables
[ WHERE conditions]
[GROUP by group_type]
[HAVING where_definition]
[ORDER BY order_type]
[LIMIT limit_criteria]
[PROCEDURE proc_name(arguments)]
[lock_options]


1. 列出列 
select name, city 
from customers;

2. 列出所有的列
select * 
from order_items;

3. 列出符合条件的列
orders 
where customerid = 3;

4. 从多个表中选出数据 // 关联
选出客户名字为Julie Smith 的所有订单
select orders.orderid, orders.amount, orders.date
from customers, orders
where
customers.name = "Julie Smith"
and customers.customerid = orders.customerid;

5.  查找订购了有关java书的客户
select customers.name
from customers, orders, order_items, books,
where customers.customerid = orders.customerid
and orders.orderid = order_items.orderid
and order_items.isbn = books.isbn
and books.title like '%Java%';


custoemrs  5
orders 3

select customers.name, orders.orderid
from customers, orders
