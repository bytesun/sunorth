from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .models import Blog,Comment
from .forms import BlogForm,CommentForm


def blog_list(request):
    allblogs = Blog.objects.filter(language=request.LANGUAGE_CODE).order_by('-createtime')[:100]
    paginator = Paginator(allblogs, 10) 
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  
    # comments = Comment.objects.all().order_by('-create_time')[:5]        
    context = {
            'blogs' : blogs,
            # 'comments' : comments,
        }
    return render(request, 'blog_list.html', context)
    
    
def blog_info(request,id):
    blog = Blog.objects.get(pk=id)
    
    relblogs = Blog.objects.filter(tags__icontains=blog.tags).exclude(id=blog.id)[:10]
    comments = Comment.objects.filter(blog=id).order_by('create_time')
    context = {
        'blog': blog,
        'relblogs' : relblogs,
        # 'owner':blog.owner,
        'comments':comments,
        'comment_form': CommentForm,

         }
    # if blog.owner == request.user:
    context['blog_form'] = BlogForm(model_to_dict(blog))         
    #init forms for case owner
    # if blog.owner == request.user:
    #     context['blog_form'] = blogForm(blog)

    return render(request, 'blog_info.html', context)
  
#new case form    
def blog_new(request):

    form = BlogForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.language=request.LANGUAGE_CODE
        instance.save()
        return redirect(instance)
    else:    
        context = {
                "form" : form,
            }
        return render(request, 'blog_new.html', context)
        
        
def blog_edit(request,id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
           form.save()
  
    return redirect(blog)
    
def comment_new(request,blogid):
    blog = Blog.objects.get(pk=blogid)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.blog=blog
        instance.save()
        
    return redirect(blog)    