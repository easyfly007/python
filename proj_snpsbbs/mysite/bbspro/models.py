from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tiezi(models.Model):
	category = models.ForeignKey('Category')
	title = models.CharField(max_length=32)
	content = models.TextField()
	author = models.ForeignKey('BBS_User')
	view_count = models.IntegerField()
	ranking = models.IntegerField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title
	
class BBS_User(models.Model):
	user = models.OneToOneField(User, unique= True)
	signature = models.CharField(max_length=20, default='nothing left')
	image = models.ImageField(upload_to = 'upload_imgs/',default='upload_imgs/default.jpg')
	def __unicode__(self):
		return self.user.username
		
class Category(models.Model):
	name = models.CharField(max_length=6, unique=True)
	administrator = models.ForeignKey(BBS_User, related_name='administrator')
	created_date  = models.DateTimeField(auto_now_add=True)
	blockedperson = models.ManyToManyField(BBS_User,related_name='blockedperson')

	def __unicode__(self):
		return self.name
