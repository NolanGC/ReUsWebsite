from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def getPosts():
    posts = Post.objects.all()
    #ret = {
    #    "main": [],
    #    "secondary": []
    #}
    #for post in posts:
    #    if(post.main_event == 1):
    #        ret["main"].append(post)
    #    else:
    #        ret["secondary"].append(post)
    return posts
def findPost(title):
	posts = Post.objects.all()
	for post in posts:
		if(post.title == title):
			return post
	return -1

def index(request):
	posts = getPosts()[:5]
	return render(request, 'reus/index.html', {'posts': posts})

def about(request):
	return render(request, 'reus/about.html')

def contact(request):
	return render(request, 'reus/contact.html')

def post(request, title):
	return render(request, 'reus/post.html', {'post': findPost(title)})