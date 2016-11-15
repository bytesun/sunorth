from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GalleryForm
from .models import Gallery
from django.conf import settings

def photo_list(request):
    allphotos = Gallery.objects.all().order_by('-createtime')[:100]
    paginator = Paginator(allphotos, 20) 
    page = request.GET.get('page')    
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        photos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        photos = paginator.page(paginator.num_pages)  
        
    context = {
        'photos':photos,
        'media_url' : settings.MEDIA_URL,
        'page':'photo'
    }    
    return render(request,'photo_list.html',context)

@login_required   
def photo_upload(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.photographer = request.user
            instance.save()
            return HttpResponseRedirect('/gallery/list')
    else:
        form = GalleryForm()
    return render(request, 'photo_upload.html', {'form': form,'page':'photo'})
    
   