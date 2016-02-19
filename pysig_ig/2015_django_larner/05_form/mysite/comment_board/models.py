from django.db import models


class Comment(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	comment = models.TextField()
	data = models.DateField()
	def __unicode__(self):
		return '%s - %s' %(self.name, self.email)