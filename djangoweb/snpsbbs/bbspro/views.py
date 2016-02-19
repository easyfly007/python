from django.shortcuts import render,render_to_response
import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from django.contrib import comments
from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login as user_login, logout as user_logout

def acc_login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	print username, password
	user = auth.authenticate(username = username, password=password)
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
	tiezi_list = models.Tiezi.objects.all()
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
	print  type(models.Tiezi.objects.get(id = tiezi_id))
	#models.Tiezi.objects.get(id = tiezi_id).update(view_count = view_count+1)
	print  models.Tiezi.objects.get(id = tiezi_id).view_count
	print tiezi_id
	user_comment= request.POST.get('comment_content')
	# comments.models.Comment.objects.create(content_type_id = 8,
	# 	object_pk = tiezi_id,
	# 	site_id =1,
	# 	user_id= request.user.id,
	# 	comment=user_comment,
	# )
	return HttpResponseRedirect('/detail/%s' % tiezi_id)

def tiezi_pub(request):
	return render_to_response('tiezi_pub.html')

def tiezi_submit(request):
	print "==>",request.POST
	author= models.BBS_User.objects.get(user__username =request.user.username)
	models.Tiezi.objects.create(
		title= request.POST.get('title'),
		content = request.POST.get('content'),
		author = author,
		view_count = 0,
		ranking = 0,
	)
	#created_tiezi_id = models.Tiezi.objects.get('title' = title)
	print models.Tiezi.objects.all()
	return HttpResponse("created successfully!<br/><a href='/index/' >back to index</a>")
	
#class UserForm(form.Form):
#	username = forms.CharField(max_length = 20)
#	password = forms.CharField(max_length=16)
#	signature = forms.CharField(max_length=20)
#	email = forms.EmailField()
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
		
		user= User()
		user.username= username
		user.password = password1
		user.save()
		models.BBS_User.objects.create(
		user = user,
		)
		
		
		#if user is not None:
		auth.login(request, user)
			#return HttpResponseRedirect('/index/')
		return HttpResponse("Register successfully!<br/><a href='/index/' >back to index</a>")
		
	
	
	
	


	
	