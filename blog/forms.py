from django import forms
from  ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea
from django.utils.encoding import force_str, force_text
from django_select2.forms import (
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)
from .models import Tag,Blog,Comment


class TaglSelect2TagWidget(ModelSelect2TagWidget):
    search_fields = [
        'name__icontains'
    ]

    queryset = Tag.objects.all()
    
    def value_from_datadict(self, data, files, name):
        values = super(TaglSelect2TagWidget, self).value_from_datadict(data, files, name)
        qs = self.queryset.filter(**{'pk__in': [l for l in values if is_int(l)]})
        names = [k.name for k in self.queryset.filter(**{'name__in': values})]
        pks = set(force_text(getattr(o, 'pk')) for o in qs)
        cleaned_values = []
        for val in values:
            if force_text(val) not in pks and force_text(val) not in names:
                val = self.queryset.create(name=val).pk
            cleaned_values.append(val)
        return cleaned_values
        
def is_int(s):
    try:
        int(str(s))
        return True
    except ValueError:
        return False
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['subject','content','tags']
        # exclude = ["owner","create_time"]
        labels = {
            
            }
        widgets = {
            'content' : CKEditorWidget(),
            'tags':TaglSelect2TagWidget
            # 'content': Textarea(attrs={'id':'ta_blog','class': 'richarea','rows': 20}),
        } 

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']          
        
