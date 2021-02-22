from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='images/')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
    	ordering = ['-date_added']

    
class quad(models.Model):
    title = models.TextField()
    highlight = models.BooleanField(default=False)
    related_link = models.URLField(max_length=255)
    body = models.TextField()
    images = models.ImageField(upload_to='images/')
    datestr = models.TextField()