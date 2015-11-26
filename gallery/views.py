from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GalleryForm

def photo_upload(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.photographer = request.user
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = GalleryForm()
    return render(request, 'photo_upload.html', {'form': form})
    
   