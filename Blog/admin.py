from django.contrib import admin
from Blog.models import Post, BlogComment

# Register your models here.
admin.site.register((Post, BlogComment))