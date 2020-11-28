from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

