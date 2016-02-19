from django.db import models
from django.contrib import admin

class Result(models.Model):
	case       =models.CharField(max_length=100, default='')
	caselist   =models.CharField(max_length=10,default='')
	rundate    =models.CharField(max_length=8,default='')
	trandiff   =models.FloatField()#'5','2')#5, 2)
	comparenote=models.CharField(max_length=10,default='')
	# comparenote shoudl be hspvsfsm, HSPICE for target and fineSim for golden
	# or fsmvshsp, FineSim for target and HSPICE for golden 
	# def __init__(self,case,caselist,rundate, trandiff,comparenote):
	# 	self.case=case
	# 	self.caselist=caselist
	# 	self.rundate=rundate
	# 	self.trandiff=trandiff
	# 	self.comparenote=comparenote

	# def __str__(self):
	# 	return self.case+' '+rundate
	# class Meta:
	# 	ordering=['-trandiff', 'case']


# admin.site.register(Result)
