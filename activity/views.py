from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
import json
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,HTTP_400_BAD_REQUEST)
from rest_framework.parsers import JSONParser
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from rest_framework.views import (
    APIView)
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    )
from django.contrib.auth.models import User
from .models import ATag,Activity,Comment
from .forms import ActivityForm,CommentForm
from .serializers import ActivitySerializer

    
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
        'otheractivities' : Activity.objects.filter(start__gte=date.today()).exclude(id=activity.id).order_by('start'),
        'comments':comments,
        'tags':activity.tags.all(),
        'comment_form': CommentForm, 
        'page':'activity'
        
         }
    #init forms for case owner
    if activity.owner == request.user:
        form = ActivityForm(model_to_dict(activity))
        form.fields['start'].initial = activity.start
        form.fields['start'].widget = forms.DateInput()        
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
    
    
    
#------------------------api--------------------------    
def activity_list_api(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    activities = Activity.objects.filter(start__gte = start, end__lte = end, language=request.LANGUAGE_CODE)
    json_list = []
    for a in activities:
        json_list.append({'id':a.id,'title': a.subject ,'start': str(a.start),'url':'/activity/'+str(a.id)+"/"})
    return HttpResponse(json.dumps(json_list), content_type='application/json')  


class ActivityApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ActivitySerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)