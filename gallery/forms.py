from django import forms
from django.forms import ModelForm
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['photo','story']
        labels = {
                'photo' : '选择照片',
                'story' : '照片说明',
            }


        
