from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import date
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Blog,Comment
from blog.forms import BlogForm
from activity.models import Activity
from gallery.models import Gallery

def home(request):
    #fetch photos
    photos = Gallery.objects.all().order_by('-createtime')[:10]
    #fetch logs
    allblogs = Blog.objects.all().order_by('-createtime')[:100]
    paginator = Paginator(allblogs, 10) 
    page = request.GET.get('page')
    comments = Comment.objects.all().order_by('-create_time')[:5]
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)  
    context = {
            'photos': photos,
            'blogs' : blogs,
            'activities' : Activity.objects.filter(do_time__gte=date.today()).order_by('do_time'),
            'comments' : comments,
            'media_url' : settings.MEDIA_URL,
        }
    return render(request, 'home.html', context)
    
