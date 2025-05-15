from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Comment

class CommentInline(GenericTabularInline):
    model = Comment
    extra = 1

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on', 'content_type', 'object_id')
    search_fields = ('author__username', 'body')