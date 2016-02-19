from django.shortcuts import render
from models import Comment 
def index(request):
	comments = Comment.object.all()
	return render(request, 'commnte_borad/index.html', locals())
	