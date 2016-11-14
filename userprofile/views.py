from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required 
def profile(request):
    context = {
         }
    return render(request, 'profile.html', context)
  

    
