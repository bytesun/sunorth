from django.shortcuts import render
from django.shortcuts import redirect

def profile(request):
    context = {
         }
    return render(request, 'profile.html', context)
  

    
