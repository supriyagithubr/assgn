from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'published_date', 'update_date']
admin.site.register(Blog,BlogAdmin)