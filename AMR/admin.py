from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin) 

from django.contrib import admin
from .models import Vehiculo

admin.site.register(Vehiculo)