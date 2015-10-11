from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

from blog.models import Blog
from blog.forms import BlogForm

def home(request):
    title='Hello'
    context = {
            'blogs' : Blog.objects.all().order_by('-createtime'),
            "title" : title,
        }
    return render(request, 'home.html', context)
    
   