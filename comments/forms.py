from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
            }),
            'body': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Write a comment...'})
        }
        labels = {
            'title': '',
            'body': ''
        }