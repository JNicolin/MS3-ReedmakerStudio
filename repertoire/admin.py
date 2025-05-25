from django.contrib import admin
from .models import Repertoire

@admin.register(Repertoire)
class RepertoireAdmin(admin.ModelAdmin):
    list_display = ("reed", "music_composer", "music_title")