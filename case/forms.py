from django import forms

from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['subject','description','tags']
        
class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()