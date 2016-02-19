from blog.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue', 
	city='Berkeley', state_province='CA', country='U.S.A.',
	website='http://www.apress.com/')
p1.save()
p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
	city='Cambridge', state_province='MA', country='U.S.A.',
	website='http://www.oreilly.com/')
p2.save()
publisher_list = Publisher.objects.all()
print publisher_list

选择,返回一个set
p = Publisher.objects.all()
// 返回一个QuerySet
p = Publisher.objects.filter(name = 'Apress')
// 返回一个name 等于 Apress 的QuerySet
p = Publisher.objects.filter(name_contains = 'press')
// 返回一个name 匹配 %press% 的QuerySet

name__startwith = 'Apre'
name__endwith =
name__icontains =


选择单个对象,用get
如果返回了多个对象，或者找不到对象，都会报错
p=Publisher.objects.get(country = 'China')

排序
p= Publisher.objects.order_by('name', 'city')
p= Publisher.objects.order_by('-name', 'city')

p= Publisher.objects 返回一个 django.db.models.manager.Manager 管理器
p= Publisher.objects.all() 返回一个QuerySet

对QuerySet能够进行的操作，也就是他的成员函数
[0]
[0:2]


更新
1. 可以先get 出来，修改之，然后save
2. 可以用update
Publisher.objects.filer(id=52).update(name = 'Apress publishing')


删除
p=...get()
p.delete()


python 里面用None
SQL里面用NULL
