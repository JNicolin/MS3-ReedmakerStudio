from django import forms
from .models import Reed, Event, Repertoire

class ReedForm(forms.ModelForm):
    class Meta:
        model = Reed
        fields = [
            'item_id', 'item_visibility', 'item_comment', 'item_type', 'item_creator', 'item_rating',
            'descr_resistance', 'descr_sound', 'descr_response','descr_length',
            'staple_model', 'staple_length', 'staple_material',
            'cane_gauge_thickness', 'cane_shaper_form', 'cane_supplier',
            'cane_gauge_thickness'
        ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['gig_title', 'gig_description', 'gig_date', 'gig_location']

class RepertoireForm(forms.ModelForm):
    class Meta:
        model = Repertoire
        fields = ['music_title', 'music_composer', 'music_genre']

        