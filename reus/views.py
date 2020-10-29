from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def frontpage(request):
	posts = Post.objects.all()
	return render(request, 'reus/frontpage.html', {'posts': posts})