from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['subject','description','tags','do_time']
        # exclude = ["owner","create_time"]
        