from django import forms
from .models import Reed, Event, Repertoire

class ReedForm(forms.ModelForm):
    class Meta:
        model = Reed
        exclude = ['created_on', 'updated_on']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

class RepertoireForm(forms.ModelForm):
    class Meta:
        model = Repertoire

        