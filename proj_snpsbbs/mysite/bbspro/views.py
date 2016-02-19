from django.shortcuts import render,render_to_response
import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import comments
from django.contrib.auth.models import User


def acc_login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username = username, password=password)
	print user
	if user is not None:
		auth.login(request,user)
		content = '''
		Welcome %s !!!
		<a href = '/logout/' >Logout</a>
		'''  % user.username
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',{'login_err':'Warning: wrong name or wrong password!'})
		
def logout_view(request):
	user= request.user
	auth.logout(request)
	return HttpResponse("<b>%s</b> logged out ! <br/><a href='/index/' >back to index</a>" % user)
	
def Login(request):
	return render_to_response('login.html')

	# Create your views here.
def index(request):
	tiezi_list = list(models.Tiezi.objects.all())
	tiezi_list.sort(cmp=None, key=lambda x:x.view_count, reverse=True)
	print tiezi_list
	#bbs_categories = models.Category.objects.all()
	return render_to_response('index.html',
														{'tiezi_list': tiezi_list,
														'user':request.user,
														}
														)

	
def tiezi_detail(request,tiezi_id):
	tiezi = models.Tiezi.objects.get(id = tiezi_id)
	return render_to_response('tiezi_detail.html',{'tiezi_obj': tiezi,'user':request.user})
	
def submit_comment(request):
	print request.POST
	tiezi_id = request.POST.get('tiezi_id')
	print "tiezi id ==>",tiezi_id
	tiezi = models.Tiezi.objects.get(id = tiezi_id)
	print tiezi.view_count
	tiezi.view_count += 1
	tiezi.save()
	print tiezi.view_count
	print models.Tiezi.objects.get(id = tiezi_id).view_count
	user_comment= request.POST.get('comment_content')
	comments.models.Comment.objects.create(content_type_id = 8,
		object_pk = tiezi_id,
		site_id =1,
		user_id= request.user.id,
		comment=user_comment,
	)
	return HttpResponseRedirect('/detail/%s' % tiezi_id)

def tiezi_pub(request):
	author= models.BBS_User.objects.get(user__username =request.user.username)
	cat_id =  request.POST.get('category_id')
	category = models.Category.objects.get(id=cat_id)
	blockedpersons = category.blockedperson.all()
	if author in blockedpersons:
		return HttpResponse('you are not allowed to post tiezi on this category!')
	return render_to_response('tiezi_pub.html',{'category':category})

def tiezi_submit(request):
	author= models.BBS_User.objects.get(user__username =request.user.username)
	cat_id = request.POST.get('cat_id')
	category = models.Category.objects.get(id = cat_id)
	print request.POST.get('category')
	models.Tiezi.objects.create(
		category = category,
		title= request.POST.get('title'),
		content = request.POST.get('content'),
		author = author,
		view_count = 0,
		ranking = 0,
	)
	print models.Tiezi.objects.all()
	return HttpResponse("created successfully!<br/><a href='/category_detail/%s'>back</a>" % cat_id)
	

def register(request):
	return render_to_response("register.html")
	
def register_create(request):
	if request.method == "POST":
		print '==>',request.POST
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		
		filter_result = User.objects.filter(username = username)
		if len(filter_result) >0:
			return render_to_response("register.html", {'errors':"Username already exists, please try another username."})
			
		if password1 != password2:
			return render_to_response('register.html',{'errors': "Two passwords differ, please try again."})
		
		user= User.objects.create_user(
		username = username,
		password = password1,
		)
		user.save
		bbsuser = models.BBS_User()
		bbsuser.user_id = user.id
		bbsuser.save()	
		return HttpResponse("Register successfully!<br/><a href='/login/' >Login</a>")
		
def show_category(request):
	category_list = list(models.Category.objects.all())
	print category_list
	return render_to_response("show_category.html",{'category_list':category_list,'user':request.user})
	
	
def category_detail(request, category_id):
	category = models.Category.objects.get(id = category_id)
	tiezi_list = list(models.Tiezi.objects.filter(category__id = category_id))
	administrator=category.administrator
	user = models.BBS_User.objects.get(user__username = request.user.username)
	if user ==administrator:
		isadministrator=True
	else:
		isadministrator=False
	return render_to_response('category_detail.html',
		{
			'category':category,
			'tiezi_list': tiezi_list,
			'user':request.user,
			'administrator':administrator,
			'isadministrator':isadministrator,}
		)

def category_mgr(request, category_id):
	category=models.Category.objects.get(id =category_id)
	administrator=category.administrator
	user = models.BBS_User.objects.get(user__username =request.user.username)
	tiezi_list = list(models.Tiezi.objects.filter(category__id = category_id))
	block_list = category.blockedperson.all()

	freeman_list = models.BBS_User.objects.all().filter
	
	return render_to_response('category_mgr.html',
		{
			'cat_id':category_id,
			'category': category,
			'administrator':administrator,
			'tiezi_list':tiezi_list,
			'block_list':block_list,
			'freeman_list':freeman_list,
		})


def tiezi_mgr(request, cat_id):
	if request.method == 'POST':
		tiezi_list=request.REQUEST.getlist('selectedtiezi')
		if len(tiezi_list)==0:
			return HttpResponse('please select at least one tiezi for delete')
		for tiezi in tiezi_list:
			tiezi = models.Tiezi.objects.get(id = int(tiezi))
			tiezi.delete()
		return HttpResponse(" totally %d tiezi deleted !<br/><a href='/category_mgr/%s' > return back</a> "  % (len(tiezi_list), cat_id) ) 
	return HttpResponse('please login as an administrator!')

# this function will set some blocked person free
def block_mgr(request, cat_id):
	if request.method =='POST':
		block_list=request.REQUEST.getlist('selectedblocked')
		category = models.Category.objects.get(id = int (cat_id))
		print category
		if len(block_list)==0:
			return HttpResponse('please select at least one user to get out of black house! <br> <a href="/category_mgr/%s"> return back </a> ' %(cat_id))
		for block in block_list:
			block = models.BBS_User.objects.get(id = int(block))
			if block in category.blockedperson.all():
				category.blockedperson.remove(block)
		return HttpResponse('set %d perple output of the black house ! <br> <a href="/category_mgr/%s" > return back </a> ' % (len(block_list), cat_id) )

# this function will send free person to the black house
def free_mgr(request, cat_id):
	names=[]
	category = models.Category.objects.get(id = int (cat_id))
	if request.method =='POST':
		if 'selectedfreeman' in request.REQUEST:
			block_list=request.REQUEST.getlist('selectedfreeman')

			for block in block_list:
				block = models.BBS_User.objects.get(id = int(block))
				if block not in category.blockedperson.all():
					print block.user.username
					category.blockedperson.add(block)
					names.append(block.user.username)
		if 'inputfreeman' in request.REQUEST:
			block_list = request.REQUEST.get('inputfreeman')
			block_list = block_list.split(' ')
			for name in block_list:
				try:
					block = User.objects.get(username = name)
				except User.DoesNotExist:
					print '%s is not a valid user name' % name
				else:
					block = models.BBS_User.objects.get(user=block)
					category.blockedperson.add(block)
					names.append(block.user.username)

	if len(names)==0:
		return HttpResponse('please select at least one user to put into the black house! <br> <a href="/category_mgr/%s" > return back </a>' % cat_id)
	else:
		return HttpResponse(' You put (%s) into the black house!<br> <a href="/category_mgr/%s" > return back </a> ' % (':'.join(names), cat_id)) 	
