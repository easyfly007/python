from django.shortcuts import render, render_to_response

def search_form(request):
	return render_to_response('search_form.html', locals())

def search(request):
	if 'q' in request.GET and request.GET['q']:
		error = 'you searched for %r' % request.GET['q']
	else:
		error = 'you searched an empty form'
	return render_to_response('search.html', locals())	
	