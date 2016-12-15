from django import forms
from  ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea
from django.utils.encoding import force_str, force_text
from django.utils.translation import ugettext as _
from .models import Club
        
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name','ctype','description','website']
        # exclude = ["owner","create_time"]
        labels = {
                "name":_("Name"),
                "ctype":_("Type"),
                "description":_("Description"),
                "website":_("Website")
            }
        widgets = {
            'description' : CKEditorWidget(),
        } 

