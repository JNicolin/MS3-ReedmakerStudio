from django import forms
from .models import Repertoire

class RepertoireForm(forms.ModelForm):
    class Meta:
        model = Repertoire
        exclude = ['created_on', 'updated_on']
        widgets = {'reed': forms.HiddenInput()}

