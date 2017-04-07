from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .models import Tag, Blog,Comment
from .forms import BlogForm,CommentForm


def blog_list(request):
    tag = request.GET.get('tag')
    allblogs = None
    if tag is not None:
        allblogs = Blog.objects.filter(tags__name__icontains=tag,language=request.LANGUAGE_CODE).order_by('-createtime')[:100]
    else:
        # allblogs = Blog.objects.filter(language=request.LANGUAGE_CODE).order_by('-createtime')[:100]
        allblogs = Blog.objects.all().order_by('-createtime')[:100]
        
    tags = Tag.objects.all()[:20]  
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
            'tags':tags,
            'page':'blog'
            # 'comments' : comments,
        }
    return render(request, 'blog_list.html', context)
    
    
def blog_info(request,id):
    blog = Blog.objects.get(pk=id)
    
    relblogs = None #= Blog.objects.filter(tags__name__in=blog.tags__name).exclude(id=blog.id)[:10]
    comments = Comment.objects.filter(blog=id).order_by('create_time')
    context = {
        'blog': blog,
        'tags': blog.tags.all(),
        'relblogs' : relblogs,
        # 'owner':blog.owner,
        'comments':comments,
        'comment_form': CommentForm,
        'page':'blog'
         }
    # if blog.owner == request.user:
    context['blog_form'] = BlogForm(model_to_dict(blog))         
    #init forms for case owner
    # if blog.owner == request.user:
    #     context['blog_form'] = blogForm(blog)

    return render(request, 'blog_info.html', context)
  
@login_required      
def blog_new(request):

    form = BlogForm(request.POST or None)
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
                'page':'blog'
            }
        return render(request, 'blog_new.html', context)
        
@login_required           
def blog_edit(request,id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
           form.save()
  
    return redirect(blog)

@login_required       
def comment_new(request,blogid):
    blog = Blog.objects.get(pk=blogid)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.blog=blog
        instance.save()
        
    return redirect(blog)    