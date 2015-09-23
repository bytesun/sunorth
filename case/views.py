from django.shortcuts import render

from case.forms import *

def cases(request):

    form = CaseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
            "form" : form,
        }
    return render(request, 'case_new.html', context)
    
