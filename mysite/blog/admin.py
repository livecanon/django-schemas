from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_modified')
    search_fields = ('title',)


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)