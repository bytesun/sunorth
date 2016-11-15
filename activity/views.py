from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime, timedelta, time
from django.conf import settings
from .models import ATag,Activity,Comment
from .forms import ActivityForm,CommentForm


def activity_list(request):
    tag = request.GET.get('tag')
    today = datetime.now().date()
    today_start = datetime.combine(today, time())
    allactivities = None
    if tag is not None:
        allactivities = Activity.objects.filter(tags__name__icontains=tag,language=request.LANGUAGE_CODE).order_by('do_time')[:100]
    else:    
        allactivities = Activity.objects.filter(do_time__gte=today_start,language=request.LANGUAGE_CODE).order_by('do_time')[:100]
        
    tags = ATag.objects.all()[:20]
    paginator = Paginator(allactivities, 20) 
    page = request.GET.get('page')    
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        activities = paginator.page(paginator.num_pages)  
        
    context = {
        'activities':activities,
        'tags':tags,
        'page':'activity'
    }    
    return render(request,'activity_list.html',context)
  
def activity_info(request,id):
    activity =Activity.objects.get(pk=id)
    comments = Comment.objects.filter(activity=id).order_by('create_time')
    context = {
        'activity': model_to_dict(activity),
        'otheractivities' : Activity.objects.filter(do_time__gte=date.today()).exclude(id=activity.id).order_by('do_time'),
        'comments':comments,
        'tags':activity.tags.all(),
        'comment_form': CommentForm, 
        'page':'activity'
        
         }
    #init forms for case owner
    if activity.owner == request.user:
        form = ActivityForm(model_to_dict(activity))
        form.fields['do_time'].initial = activity.do_time
        form.fields['do_time'].widget = forms.DateInput()        
        context['activity_form'] = form

    return render(request, 'activity_info.html', context)
  
@login_required     
def activity_new(request):

    form = ActivityForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.language=request.LANGUAGE_CODE
        instance.save()
        form.save_m2m()
        return redirect(instance)
    else:    
        context = {
                "form" : form,
                'page':'activity'
            }
        return render(request, 'activity_new.html', context)
        
@login_required            
def activity_edit(request,id):
    activity = Activity.objects.get(pk=id)
    if request.method == 'POST':
        form =ActivityForm(request.POST, instance=activity)
        if form.is_valid():
           form.save()
  
    return redirect(activity)

@login_required        
def comment_new(request,activityid):
    activity = Activity.objects.get(pk=activityid)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.activity=activity
        instance.save()
        
    return redirect(activity)     