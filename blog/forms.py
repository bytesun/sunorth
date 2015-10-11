from django import forms
from django.forms import ModelForm, Textarea
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['subject','content','tags']
        # exclude = ["owner","create_time"]
        widgets = {
            'content': Textarea(attrs={'class': 'richarea','rows': 20}),
        }             
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']          