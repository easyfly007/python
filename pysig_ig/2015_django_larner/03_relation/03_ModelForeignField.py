from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=20)
	father = models.ForeignKey('self')


class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
'''	
class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey('Author')

class Author(models.Model):
	name = models.CharField(max_length=20)

'''


很遗憾，
因为syncdb仅仅创建数据库里还没有的表，它 并不 对你数据模型的修改进行同步,也不处理数据模型的删除。
我们需要手动drop原先的table，然后用syncdb来创建新的表

创建数据表
cmd > python manage.py syncdb 
显示create table调用
cmd > python manage.py sql  
从sql文件中初始化数据载入语句
cmd > python manage.py sqlall
创建索引
cmd > python manage.py sqlindexes
显示drop table 调用
cmd > python manage.py sqlclear
显示drop table 和 create table的组合
cmd > python manage.py sqlreset

sql**语句并不改变数据库，而是打印相应的命令，你可以自己去run



# get a book
book = Book.objects.get(title='django book')
# get the book's author 
author = book.author
# get all the books related with the author 
books = author.book_set.all()



# 以上仅限于只有单个foreign key的情况
# 如果有多个foreignKey，需要指定 related_name
class Book(models.Model):
	author = models.ForeignKey('Author', related_name = 'books')

book = Book.objects.get(title='django book')
author = book.author
books = author.books.all()


如何在MySQl中查看：
1. MySQL console
2. python manager.py dbshell
（请将MySQL bin目录添加到path环境变量中去）

# 在MySQL中查看，key分三种，
1. 空 ：值可重复，没有索引
2. PRI：主键， 
3. UNI：唯一
4. MUL：值可重复，该列是一个非唯一索引的前导列(第一列)或者是一个唯一性索引的组成部分但是可以含有空值NULL
非唯一索引
firstname + lastname 可以作为索引，但是单独的firstname或者lastname不能。
外键

