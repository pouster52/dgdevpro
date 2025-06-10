from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "title", "created_date", "published_date")