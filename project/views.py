from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import date
from django.conf import settings

from blog.models import Blog,Comment
from blog.forms import BlogForm
from activity.models import Activity
from gallery.models import Gallery

def home(request):
    #fetch photos
    photos = Gallery.objects.all().order_by('-createtime')[:10]
    #fetch logs
    
    # blogs = Blog.objects.filter(language=request.LANGUAGE_CODE).order_by('-createtime')[:10]
    blogs = Blog.objects.filter(language='zh-CN').order_by('-createtime')[:10]

    context = {
            'photos': photos,
            'blogs' : blogs,
            'activities' : Activity.objects.filter(do_time__gte=date.today(),language=request.LANGUAGE_CODE).order_by('do_time'),
            'media_url' : settings.MEDIA_URL,
        }
    return render(request, 'home.html', context)
    
def club(request):
    return render(request, 'club.html', {});