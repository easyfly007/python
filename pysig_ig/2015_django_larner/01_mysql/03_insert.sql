
MySQL 插入数据


INSERT into customers values
(NULL, 'yifei huang', 'zhaofeng palza', 'Shanghai');

INSERT into customers (name, city) values
('Yhu', 'china');

INSERT into customers
set name ='Daniel',
    address = '1027 changning rd',
    city = 'beijing';

可以通过脚本文件来导入数据库中运行命令
比如> mysql -h localhost -u bookorama -p books < /path/to/book_insert.sql