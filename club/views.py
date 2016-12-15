from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings
from .models import Club
from .forms import ClubForm


def list(request):
    form = ClubForm()
    clubs = Club.objects.filter(language=request.LANGUAGE_CODE)
    context = {
        'form':form,
        'clubs':clubs
    }
    return render(request, 'club.html', context);
    
def add(request):
    if request.method == "POST":
        form = ClubForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.language=request.LANGUAGE_CODE
            instance.save()
    return redirect('club_list')
    