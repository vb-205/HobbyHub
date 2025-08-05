from django.contrib import admin
from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'group', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'group')
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content', 'post__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)