from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)

class PostModelAdmin(admin.ModelAdmin):

    search_fields = ('title', 'text', 'snippet', 'category__name')