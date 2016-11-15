from django.core.mail import send_mail
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User 
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from datetime import date
from django.conf import settings
from django.utils.translation import ugettext as _

from blog.models import Blog,Comment
from blog.forms import BlogForm
from activity.models import Activity
from gallery.models import Gallery

def home(request):
    #fetch photos
    photos = Gallery.objects.all().order_by('-createtime')[:10]
    #fetch logs
    
    blogs = Blog.objects.filter(language=request.LANGUAGE_CODE).order_by('-createtime')[:10]
    # blogs = Blog.objects.filter(language='zh-CN').order_by('-createtime')[:10]

    context = {
            'photos': photos,
            'blogs' : blogs,
            # 'activities' : Activity.objects.filter(do_time__gte=date.today(),language=request.LANGUAGE_CODE).order_by('do_time'),
            'media_url' : settings.MEDIA_URL,
        }
    return render(request, 'home.html', context)
    
def registform(request):
    message = ""
    mtype = "info"
    if request.method == 'POST':
        username = request.POST.get('username')
        
        try:
            user = User.objects.get(username__iexact=username)
            message = _('The user account is existed! You can login now.')
            return render(request, 'login.html', {'message':message,'mtype':mtype})    
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                password='',
                email=username
            )    
            password = User.objects.make_random_password()
            user.set_password(password)
            user.is_active=False
            user.save()
            #send email for activate
            template_html = 'email_template.html'
            template_text = 'email_template.txt'        
            to = username
            from_email = settings.DEFAULT_FROM_EMAIL           
            subject = _('Activate your Vansday account')
            text = _(' Thanks for you register Vansday.net, please click or copy the link to activate your Vansday account : http://'+Site.objects.get_current().domain+'/activate?id='+username+"&code="+password)
    
            text_content = loader.render_to_string(template_text, {"subject": subject,"greeting":_("Hello!"),"text": text,"signature":_("Vansday Team"),"domain":Site.objects.get_current().domain})
            html_content = loader.render_to_string(template_html, {"subject": subject,"greeting":_("Hello!"),"text": text,"signature":_("Vansday Team"),"domain":Site.objects.get_current().domain})
    
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()     
            #display message    
            message =  _('Thanks for your registration! Please check your email to activate your account.')
            return render(request, 'message.html', {'message':message,'mtype':mtype})
    return render(request, 'login.html', {})    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active == True:
           login(request,user)
           redirecto = request.POST.get('redirecto')
           print(redirecto)
           if redirecto != 'None' :
               return redirect(redirecto)
           else:
               return redirect('home')
        else:
           return render(request, 'login.html', {'message':_('Your username or password is wrong, please try again!'),'mtype':'error'})
    else:
        redirecto = request.GET.get('next')
        # if request.user.is_authenticated():
        #     return redirect('profile')
    return render(request, 'login.html', {'redirecto':redirecto})    

def resetpwd(request):
    if request.method == 'POST':
        password = User.objects.make_random_password()
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=email)
            user.set_password(password)
            user.save()
            #send email
            template_html = 'email_template.html'
            template_text = 'email_template.txt'        
            to = email
            from_email = settings.DEFAULT_FROM_EMAIL           
            subject = _('Reset Password')
            text =  _('Please click the link to reset your password: https://'+Site.objects.get_current().domain+'/resetpwd')+"?id="+email+"&code="+password
    
            text_content = loader.render_to_string(template_text, {"subject": subject,"greeting":_("Hello!"),"text": text,"signature":_("Vansday Team"),"domain":Site.objects.get_current().domain})
            html_content = loader.render_to_string(template_html, {"subject": subject,"greeting":_("Hello!"),"text": text,"signature":_("Vansday Team"),"domain":Site.objects.get_current().domain})
    
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send() 
            
            
            return render(request,'message.html',{'message':_('Please check your email for reseting password!'),'mtype':'info'})        
        except User.DoesNotExist:
            return render(request,'message.html',{'message':_('This user is not existed!')})
       
    else:
        uid=request.GET.get('id')
        code=request.GET.get('code')
        if uid and uid is not 'None':
            user = authenticate(username=uid, password=code)
            login(request,user)  
            title = _('Reset Password')
            return render(request, 'chpwd.html',{'title':title})

        return render(request,'resetpwd.html',{'title':_('Reset Password')})
    

def activate(request):
    username = request.GET.get('id')
    password = request.GET.get('code')
    user = User.objects.get(username__iexact=username)
    
    if user.check_password(password):
        user = authenticate(username=username, password=password)
        user.is_active=True
        user.save()
        if user is not None and user.is_active == True:
            login(request,user)        
        return redirect('chpwd')
    else:
        return render(request, 'login.html',{'message':_('Your password is wrong, you can reset password using "forget password" function as below.')})
        
        
@login_required    
def chpwd(request):
    user = request.user
    message = ''
    title = _('Change Password')
    # user = User.objects.get(username__iexact=request.user.username)        
    if request.method == 'POST':
        newpwd = request.POST.get('newpwd')
        cfpwd = request.POST.get('cfpwd')

        if newpwd != cfpwd:
           message=_('Your confirm password is not same with New Password!')
           title = _('Reset Password')
        else:    
            user.set_password(newpwd)
            update_session_auth_hash(request, user)
            user.save()
            return redirect('profile')

    return render(request, 'chpwd.html',{'message':message,'title':title})

@login_required  
def logoff(request):
    logout(request)
    return redirect('home')
    
def club(request):
    return render(request, 'club.html', {});
    
    