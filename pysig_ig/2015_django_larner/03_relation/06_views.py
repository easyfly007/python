from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from myapp.models import Publisher, Book, Author
from myapp.forms import AuthorForm, PublisherForm, BookForm

def index(request):
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()
	return render_to_response('index.html', locals() , context_instance = RequestContext(request))


def new_publisher(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = PublisherForm(request.POST)
	if form.is_valid():
		form.save()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def new_author(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = AuthorForm(request.POST)
	if form.is_valid():
		form.save()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def new_book(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = BookForm(request.POST)
	if form.is_valid():
		form.save()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))



def update_author(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = AuthorForm(request.POST)
	if 'author_id' in request.POST:
		author_id = request.POST['author_id']
		# author = Author.objects.get(id=author_id)
		if form.is_valid():
			print 'update author input valid'
			cd = form.cleaned_data
			Author.objects.filter(id=author_id).update(first_name=cd['first_name'], last_name=cd['last_name'], email = cd['email'])
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def update_publisher(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = PublisherForm(request.POST)
	if 'publisher_id' in request.POST:
		publisher_id=request.POST['upd_id']
		if form.is_valid():
			cd = form.cleaned_data
			Publisher.objects.filter(id= publisher_id).update(name = cd['name'], address=cd['address'], city=cd['city'], state_province=cd['state_province'],country=cd['country'], website=cd['website'])
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def update_book(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	form = BookForm(request.POST)
	if 'book_id' in request.POST:
		book_id = request.POST['book_id']
		if form.is_valid():
			print 'update book input valid'
			cd = form.cleaned_data
			Book.objects.filter(id=book_id).update(title=cd['title'], authors=cd['authors'], publisher=cd['publisher'], publication_date=cd['publication_date'])
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))


def delete_publisher(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	if 'publisher_id' in request.POST:
		publisher_id = request.POST['publisher_id']
		publisher = Publisher.objects.get(id=publisher_id)
		publisher.delete()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def delete_author(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	if 'author_id' in request.POST:
		author_id = request.POST['author_id']
		author = Publisher.objects.get(id=author_id)
		author.delete()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
def delete_book(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	if 'book_id' in request.POST:
		book_id = request.POST['book_id']
		book = Publisher.objects.get(id=book_id)
		book.delete()
	new_author_form = AuthorForm()
	new_publisher_form = PublisherForm()
	new_book_form = BookForm()		
	publisher_list = Publisher.objects.all()
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def recommend_book(request):
	book_list = Book.objects.all()
	if request.method == 'GET':
		return render_to_response('recommend.html', locals(), context_instance = RequestContext(request))
	if request.method =='POST' and 'book_id' in request.POST:
		book_id = request.POST['book_id']
		book = Book.objects.get(id =book_id)
		publisher = book.publisher
		authors = book.authors.all()
		recommends = Book.objects.all().filter(publisher = publisher)
		recommends = recommends.exclude(id=book_id)	
	return render_to_response('recommend.html', locals(), context_instance = RequestContext(request))