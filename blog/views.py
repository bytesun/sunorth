from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict

from django.conf import settings
from .models import Blog,Comment
from .forms import BlogForm,CommentForm


    

def blog_info(request,id):
    blog = Blog.objects.get(pk=id)
    comments = Comment.objects.filter(blog=id).order_by('create_time')
    context = {
        'blog': blog,
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