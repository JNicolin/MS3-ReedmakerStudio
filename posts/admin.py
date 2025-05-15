from django.contrib import admin
from .models import Post
from comments.admin import CommentInline

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "excerpt", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]
