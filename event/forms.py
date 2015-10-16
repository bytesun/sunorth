from django import forms
from  ckeditor.widgets import CKEditorWidget
from .models import Event,Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['subject','description','tags','do_time']
        # exclude = ["owner","create_time"]
        labels = {
            'subject':'Event',
            'do_time': 'Date',
        }
        widgets = {
            'description' : CKEditorWidget(),
            'do_time' : forms.TextInput(attrs={'type': 'date'}),
            # 'content': Textarea(attrs={'id':'ta_blog','class': 'richarea','rows': 20}),
        } 
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']          
                