from django.contrib import admin
from runresult.models import Result

class ResultAdmin(admin.ModelAdmin):
	list_display=('case','caselist','rundate','comparenote','trandiff')
	list_filter=('caselist','comparenote','rundate')

admin.site.register(Result, ResultAdmin)


