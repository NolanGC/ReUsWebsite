from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import quad

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

def getQuads():
    """ [highlight, rest] """
    from .models import quad
    ret = [[],[]]
    quads = quad.objects.all()
    for quad in quads:
        if(quad.highlight):
            ret[0].append(quad)
        else:
            ret[1].append(quad)
    return ret

    

def index(request):
	posts = getPosts()[:5]
	return render(request, 'reus/index.html', {'posts': posts})

def about(request):
	return render(request, 'reus/about.html')

def quad(request):
    quads = getQuads()
    return render(request, 'reus/quad.html', {'previous': quads[1], 'next': quads[0][0]})

def post(request, title):
	return render(request, 'reus/post.html', {'post': findPost(title)})