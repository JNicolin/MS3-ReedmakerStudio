from django.contrib import admin
from .models import Reed
from comments.admin import CommentInline

@admin.register(Reed)
class ReedAdmin(admin.ModelAdmin):
    list_display = ("item_id", "item_creator", "item_comment", "item_visibility", "created_on")
    inlines = [CommentInline]