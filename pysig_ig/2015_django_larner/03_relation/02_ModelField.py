

from django.db import models
class Book(models.Model):
	title = CharField(max_length =100)
	content = TextField()
	published = BooleanField()

class Author(models.Model):
	email = EmailField()
	personalweb = URLField()
	alive = NullBooleanField()
	resume = FileField()


