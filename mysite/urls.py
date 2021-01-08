"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('', include('reus.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from reus.models import Post
from django.conf.urls.static import static
from django.conf import settings
def getPosts():
    posts = Post.objects.all()
    ret = {
        "main": [],
        "secondary": []
    }
    for post in posts:
        if(post.main_event == 1):
            ret["main"].append(post)
        else:
            ret["secondary"].append(post)
    return ret

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='reus/frontpage.html', 
        extra_context={"main": getPosts()["main"][0], "posts": getPosts()["secondary"],}
    )),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)