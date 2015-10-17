from django import forms
from  ckeditor.widgets import CKEditorWidget
from .models import Activity,Comment

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['subject','description','tags','do_time']
        # exclude = ["owner","create_time"]
        labels = {
            'subject':'Activity',
            'do_time': 'Date',
        }
        widgets = {
            'description' : CKEditorWidget(),
            'do_time' : forms.DateInput(attrs={'type': 'date'},format=('%d-%m-%Y')),

            # 'content': Textarea(attrs={'id':'ta_blog','class': 'richarea','rows': 20}),
        } 
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']          
                