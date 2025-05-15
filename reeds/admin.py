from django.contrib import admin
from .models import Reed, Event, Repertoire
from comments.admin import CommentInline

# Register your models here.
admin.site.register(Event)
admin.site.register(Repertoire)

@admin.register(Reed)
class ReedAdmin(admin.ModelAdmin):
    list_display = ("item_id", "item_creator", "item_comment", "item_visibility", "created_on")
    inlines = [CommentInline]
