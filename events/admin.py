from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("reed", "gig_date", "gig_title", 'gig_location', 'gig_description')