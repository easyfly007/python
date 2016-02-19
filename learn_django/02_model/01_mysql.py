from django.shortcuts import render_to_response
import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})


# 1. run below command in the python shell
import MySQLdb
db = MySQLdb.connect(user = 'root', db='books', host='localhost')
cursor = db.cursor()
execute= 'select * from customers order by name;'
cursor.execute(execute)
names = cursor.fetchall()
print names

names = cursor.fetchall()
print names

db.close()


# 2. create model class <==> SQL table
# see models.py