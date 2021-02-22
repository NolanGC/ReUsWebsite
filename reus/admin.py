from django.contrib import admin
from .models import Post
from .models import quad

admin.site.register(quad)
admin.site.register(Post)