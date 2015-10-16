from django import forms
from  ckeditor.widgets import CKEditorWidget
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['subject','description','tags','do_time']
        # exclude = ["owner","create_time"]
        widgets = {
            'description' : CKEditorWidget(),
            
            # 'content': Textarea(attrs={'id':'ta_blog','class': 'richarea','rows': 20}),
        } 