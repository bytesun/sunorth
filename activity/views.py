from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from datetime import date
from django.conf import settings
from .models import Activity,Comment
from .forms import ActivityForm,CommentForm

  
def activity_info(request,id):
    activity =Activity.objects.get(pk=id)
    comments = Comment.objects.filter(activity=id).order_by('create_time')
    context = {
        'activity': model_to_dict(activity),
        'comments':comments,
        'comment_form': CommentForm,        
         }
    #init forms for case owner
    if activity.owner == request.user:
        context['activity_form'] = ActivityForm(model_to_dict(activity))

    return render(request, 'activity_info.html', context)
  
#new case form    
def activity_new(request):

    form = ActivityForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.save()
        return redirect(instance)
    else:    
        context = {
                "form" : form,
            }
        return render(request, 'activity_new.html', context)
        
        
def activity_edit(request,id):
    activity = Activity.objects.get(pk=id)
    if request.method == 'POST':
        form =ActivityForm(request.POST, instance=activity)
        if form.is_valid():
           form.save()
  
    return redirect(activity)
    
def comment_new(request,activityid):
    activity = Activity.objects.get(pk=activityid)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.activity=activity
        instance.save()
        
    return redirect(activity)     