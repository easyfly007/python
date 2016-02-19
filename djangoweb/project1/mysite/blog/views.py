from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext

from blog.models import Book

def book_list(request):
	books = Book.objects.order_by('name')
	return render_to_response('book_list.html', {'books':books})

def index(request):
	return HttpResponse('welcome to %s' %request.get_host())

def request_list(request):
	host = request.get_host()
	path = request.path
	full_path = request.get_full_path()
	is_secure = request.is_secure()
	# metas = request.META.items()
	# for k, v in metas:
	# 	print k, '==', v
	# res= '<table> <tr> <th> key </th> <th> value</th></tr>'
	# for key, val in metas:
	# 	res +=  "<tr><td>" + key + " </td> <td>"+ val +" <td> </tr>"
	# res = res+"</table>"
	# return HttpResponse(res)
	# return render_to_response('request_list.html', locals())
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
	return render_to_response('search_form.html', locals(), context_instance = RequestContext(request))

def search(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/index')
	error = False
	if 'q' in request.POST:
		if request.POST['q']:
			q = request.POST['q']
			books = Book.objects.filter(title__icontains = q)
			html = []
			html.append('result:')
			for book in books:
				html.append(book.title)
		else:
			error = True
	else:
		error = True

	# return render_to_response('search_result.html', locals())
	# 		return render_to_response('search_form.html', locals(),context_instance = RequestContext(request))
	# else:
	return render_to_response('search_form.html', locals(),context_instance = RequestContext(request))

def indexx(request, temp):
	return render_to_response(temp, locals())

def blogindex(request):
	return HttpResponse('blogindex')

