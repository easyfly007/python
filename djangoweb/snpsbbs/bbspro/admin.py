from django.contrib import admin
from bbspro import models

class Tiezi_admin(admin.ModelAdmin):
	list_display = ('title','author','sig','view_count','created_date','updated_date')
	list_filter=('created_date',)
	search_fields=('title','author__user__username')
	def sig(self,obj):
		return obj.author.signature
	sig.short_description = 'signature'


	
admin.site.register(models.Tiezi,Tiezi_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_User)
