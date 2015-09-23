from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

from case.forms import *

def home(request):
    title='Hello'
    context = {
            "title" : title,
        }
    return render(request, 'home.html', context)
    
    
    
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        subject = 'hello'
        from_email =  settings.EMAIL_HOST_USER
        to_email = [email]
        contact_message = 'hello %s %s '% (full_name , message)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=True
        )
        
    contaxt = {
        "form":form
    }
    return render(request,'forms.html',contaxt)