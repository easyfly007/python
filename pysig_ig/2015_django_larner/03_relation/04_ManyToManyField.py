foreign key:
	1 book   ==> 1 author
	1 author ==> many books

ManyToManyField()
	1 book   ==> many authors
	1 author ==> namy books
因为关系是对称的，所以在无论哪一端定义都没有关系
# admin中，只有定义的一端才会显示


记得先drop table，再syncdb

from django.db import models
class Author(models.Model):
	name = models.CharField(max_length=20)

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.ManyToManyField('Author')


查看数据库，django帮我们多建立了一张表关系查找表，对django是隐藏的
table myapp_book
table myapp_author
table myapp_book_author
MUL 代表外键

试着把三个table删除了
drop table的以来关系
必须要先删除 myapp_boook_author
drop table myapp_author, myapp_book_author, myapp_book
>> error
drop table myapp_book_author, myapp_author, myapp_book
>> OK



book = Book.objects.get(title='django book')

# get the books' authors
authors = Book.author_set.all()

books =authors[2].book_set.all()

QuerySet()


book_set.all()
book_set.filter(expr)
book_set.exclude(expr)
book_set.get(expr)
book_set.order_by('title')
# QuerySet 
# dark typing

expr 可以是：
title__in
title__gt
title__gte
title__lt
title__lte
title__contains
title__last
请查阅官方文档找到每一个方法
book_set.filter(expr1, expr2)
https://docs.djangoproject.com/en/dev/ref/models/querysets/

QuerySet 看做一个容器，能够迭代，切片，索引，获取长度 


