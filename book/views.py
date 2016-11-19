from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_select2.forms import (
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)
from django.conf import settings
from .models import BTag, Book,BComment
from .forms import BookForm,BCommentForm


def book_list(request):
    tag = request.GET.get('tag')
    allbooks = None
    if tag is not None:
        allbooks = Book.objects.filter(tags__name__icontains=tag,language=request.LANGUAGE_CODE).order_by('-createtime')[:100]
    else:
        allbooks = Book.objects.filter(language=request.LANGUAGE_CODE).order_by('-createtime')[:100]
        
    tags = BTag.objects.filter(language=request.LANGUAGE_CODE)  
    paginator = Paginator(allbooks, 10) 
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)  
    # comments = Comment.objects.all().order_by('-create_time')[:5]        
    context = {
            'books' : books,
            'tags':tags,
            'page':'book'
            # 'comments' : comments,
        }
    return render(request, 'book_list.html', context)
    
    
def book_info(request,id):
    book = Book.objects.get(pk=id)
    
    relbooks = None #= book.objects.filter(tags__name__in=book.tags__name).exclude(id=book.id)[:10]
    comments = BComment.objects.filter(book=id).order_by('create_time')
    context = {
        'book': book,
        'tags': book.tags.all(),
        'relbooks' : relbooks,
        # 'owner':book.owner,
        'comments':comments,
        'comment_form': BCommentForm,
        'page':'book'
         }
    # if book.owner == request.user:
    context['book_form'] = BookForm(model_to_dict(book))         
    #init forms for case owner
    # if book.owner == request.user:
    #     context['book_form'] = bookForm(book)

    return render(request, 'book_info.html', context)
  
@login_required      
def book_new(request):

    form = BookForm(request.POST or None)
    form.fields['tags'].widget = Select2MultipleWidget()
    form.fields['tags'].queryset = BTag.objects.filter(language=request.LANGUAGE_CODE)
    
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
                'page':'book'
            }
        return render(request, 'book_new.html', context)
        
@login_required           
def book_edit(request,id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
           form.save()
  
    return redirect(book)

@login_required       
def comment_new(request,bookid):
    book = Book.objects.get(pk=bookid)
    form = BCommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner=request.user
        instance.book=book
        instance.save()
        
    return redirect(book)    