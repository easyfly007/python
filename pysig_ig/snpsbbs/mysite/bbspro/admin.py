from django.contrib import admin
from bbspro import models

class Tiezi_admin(admin.ModelAdmin):
	list_display = ('title','author','sig','category','view_count','created_date','updated_date')
	list_filter=('created_date',)
	search_fields=('title','author__user__username')
	def sig(self,obj):
		return obj.author.signature
	sig.short_description = 'signature'

class Category_admin(admin.ModelAdmin):
	list_display = ('name','administrator','created_date')
	list_filter=('created_date',)
	search_fields=('name','administrator')

	
admin.site.register(models.Tiezi,Tiezi_admin)
admin.site.register(models.Category, Category_admin)
admin.site.register(models.BBS_User)

