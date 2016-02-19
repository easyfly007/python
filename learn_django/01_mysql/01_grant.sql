一个数据库相当于一个文件夹，一个数据表相当于一个文件

0. 登录 MySQL服务器
mysql -h hostname -u username -p
-h表示主机，在本地的可以用localhost
-u 表示用户，比如root
-p 表示登录时需要密码，如果未设置密码，可以忽略

1. 创建数据库
创建名为 books的数据库
CREATE database books;


2. 设置用户与权限
GRANT 授权，REVOKE 取消授权
权限包括：
SELECT 选择 INSERT 插入 UPDATE 跟新 DELETE 删除
以及 INDEX 建立索引 ALTER 更改表的结构 CREATE 创建数据库或者表 DROP 删除数据库或者表
创建管理员
GRANT all on * to fred identified by '123abc' with grant option;
创建了一个叫做fred的用户，密码是123abc，能够操作所有的数据库（* 指定）以及有所有的权限（all指定），并允许他向其他用户授权。

撤销用户 fred
revoke all privileges, grant from fred;

针对数据库 books 创建没有任何权限的用户 sally, 
GRANT usage on books.* to sally identified by 'sally123';

给予sally适当的授权
GRANT select, insert, update, delete, index, alter, create, drop on books.* to sally;

撤销给sally的部分授权
REVOKE alter, create, drop on books.* from sally;

撤销对sally的所有授权
REVOKE all on books.* from sally;


3. 创建数据库表 TABLE

CREATE table customers(
customerid int unsigned not null auto_increment primary key,
name char(50) not null,
address char(100) not null,
city char(30) not null
);
请参考 bookoroma.sql 


4. 其他的一些操作
指定数据库
use books; 
显示数据表
show tables;
查看数据表books 的column
show columns form books; 
