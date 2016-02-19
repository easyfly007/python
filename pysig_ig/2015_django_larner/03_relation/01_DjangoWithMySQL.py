1.0
确认MySQLdb在python中已经被安装了


cmd> python
>>> import MySQLdb

1.1 在django中新建项目
cmd> python C:\Python27\Lib\site-packages\Django-1.8-py2.7.egg\django\bin\django-admin.py startproject myproj
cmd> cd myproj
cmd> python manage.py startapp myapp

1.2 打开MySQL对话框，输入
  start wamp server
cmd> cd C:\wamp\bin\mysql\mysql5.5.20\bin
cmd> mysql -u root -h localhost -p
passwd> ***
如果需要支持中文，字符集改为 utf-8
MySQL > create database myprojdb default character set utf8;
MySQL > alter database  myprojdb character set utf8;
MySQL > grant all on myprojdb.* to myprojusr identified by 'myproj123';


# 1.3 修改setting.py
# 1.3.1 install app
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
)
'''
1.3.2 修改db的配置
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myprojdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


'''
1.4 在models.py 中创建类
'''
from django.db import models
# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length= 30)


1.5 运行命令 syncdb, 同步数据库
添加auth system，用户系统，
创建超级用户
cmd> python manage.py syncdb
cmd> python manage.py makemigrations
cmd> python manage.py migrate



1.6 在mysql中查看生成的表格
mysql > use myprojdb;
mysql > show tables;
mysql > describe myapp_customer;


1.7 删除匿名用户
MySQL> UPDATE user set password=PASSWORD('your password') where user='';
MySQL> delete from mysql.user where user=''
MySQL> FLUSH PRIVILEGES;

1.8 MySQL文件在哪里？
C:\wamp\bin\mysql\mysql5.5.20\data
