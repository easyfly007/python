from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from myapp.models import Customer


def index(request):
	cust_list = Customer.objects.all()
	return render_to_response('index.html', locals() , context_instance = RequestContext(request))


def insert(request):
	if request.method == 'GET':
			return HttpResponseRedirect('/index')
	warning = 'insert OK'
	name = request.POST['new_name']
	city = request.POST['new_city']
	address = request.POST['new_address']
	if len(name) == 0:
		warning = 'Insert new customer failed, please full fill the new cust form'
		return render_to_response('index.html', locals(), context_instance = RequestContext(request))		
	else:
		newcust = Customer()
		newcust.name = name
		newcust.city = city
		newcust.address = address
		newcust.save()
	cust_list = Customer.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))


def update(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	warning = 'update OK'
	upd_id = int(request.POST['upd_id'])
	upd_name = request.POST['upd_name']
	upd_city = request.POST['upd_city']
	upd_address = request.POST['upd_address']
	if len(upd_name)==0:
		warning = 'update customer failed, customer name cannot be empty'
	else:
		Customer.objects.filter(id=upd_id).update(name=upd_name, city=upd_city, address = upd_address)
	cust_list = Customer.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))


def delete(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	warning ='delete OK'
	del_id = int(request.POST['del_id'])
	cust = Customer.objects.get(id=del_id)
	cust.delete()
	cust_list = Customer.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))