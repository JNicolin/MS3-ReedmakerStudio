from django import forms
from .models import Reed

class ReedForm(forms.ModelForm):
    class Meta:
        model = Reed
        exclude = ['created_on', 'updated_on']
