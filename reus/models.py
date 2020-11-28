from django.db import models

# Create your models here.
class Post(models.Model):
    main_event = models.IntegerField()
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='images/')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ['-date_added']
