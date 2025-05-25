from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['created_on', 'updated_on']
        widgets = {'reed': forms.HiddenInput()}
