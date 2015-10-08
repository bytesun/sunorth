from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.conf import settings
from .models import Event
from .forms import EventForm
# Create your views here.
def event_list(request):
    context = {
            'media_url' : settings.MEDIA_URL,
            'events' : Event.objects.all()
        }
    return render(request, 'event_list.html', context)
    
  
def event_info(request,id):
    event = Event.objects.get(pk=id)
    
    context = {
        'event': model_to_dict(event),
         }
    #init forms for case owner
    # if event.owner == request.user:
    #     context['event_form'] = EventForm(event)

    return render(request, 'event_info.html', context)
  
#new case form    
def event_new(request):

    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.save()
        return redirect(instance)
    else:    
        context = {
                "form" : form,
            }
        return render(request, 'event_new.html', context)
        
        
def event_edit(request,id):
    event = Event.objects.get(pk=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
           form.save()
  
    return redirect(event)
    