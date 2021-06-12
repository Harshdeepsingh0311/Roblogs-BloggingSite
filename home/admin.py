from django.contrib import admin
from .models import Contact

admin.site.site_header = "Roblogs Admin Panel"

# Register your models here.
admin.site.register(Contact)