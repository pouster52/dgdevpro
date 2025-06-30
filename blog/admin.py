from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_diplay = ("author", "title", "text", "created_date", "published_date")