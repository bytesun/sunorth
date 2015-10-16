from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Blog
from blog.forms import BlogForm

def home(request):
    allblogs = Blog.objects.all().order_by('-createtime')[:100]
    paginator = Paginator(allblogs, 10) 
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)  
    context = {
            'blogs' : blogs,

        }
    return render(request, 'home.html', context)
    
