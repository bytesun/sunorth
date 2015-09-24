from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings



def home(request):
    title='Hello'
    context = {
            "title" : title,
        }
    return render(request, 'home.html', context)
    
   