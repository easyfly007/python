1. models.py， model类 <==> sql table

2. syncdb，生成了 sql文件(保存于硬盘，而不是内存)

3. 手动insert
// run python manager.py shell
from cust.models import Customers
customerlist = Customers.objects.all()
print customerlist

newcust = Customers(name = 'tom', address = 'tom street', city = 'hongkong')
newcust.save()

customerlist = Customers.objects.all()
print customerlist




4. 通过web 提交的insert
// file views.py


