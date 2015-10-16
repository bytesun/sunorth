from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.conf import settings
from .models import Event,Comment
from .forms import EventForm,CommentForm
# Create your views here.
def event_list(request):
    context = {
            'media_url' : settings.MEDIA_URL,
            'events' : Event.objects.all()
        }
    return render(request, 'event_list.html', context)
    
  
def event_info(request,id):
    event = Event.objects.get(pk=id)
    comments = Comment.objects.filter(event=id).order_by('create_time')
    context = {
        'event': model_to_dict(event),
        'comments':comments,
        'comment_form': CommentForm,        
         }
    #init forms for case owner
    if event.owner == request.user:
        context['event_form'] = EventForm(model_to_dict(event))

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
    
def comment_new(request,eventid):
    event = Event.objects.get(pk=eventid)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.event=event
        instance.save()
        
    return redirect(event)     