from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length= 30)

