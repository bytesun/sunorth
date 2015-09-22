from django import forms

from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['subject','description','tags']
        