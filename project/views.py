from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from httplib2 import Http,urllib
from blog.models import Blog
from blog.forms import BlogForm

def home(request):
    allblogs = Blog.objects.all().order_by('-createtime')[:100]
    paginator = Paginator(allblogs, 10) 
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)  
    context = {
            'blogs' : blogs,

        }
    return render(request, 'home.html', context)
    
   
# def google_login(request):
#     token_request_uri = "https://accounts.google.com/o/oauth2/auth"
#     response_type = "code"
#     client_id = '876151127490-u1kt7kepcffhhqtfpj4snf5cajn7q7o5'
#     redirect_uri = 'http://sun-python-bytesun.c9.io/soc/complete/google-oauth2/'
#     scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
#     url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
#         token_request_uri = token_request_uri,
#         response_type = response_type,
#         client_id = client_id,
#         redirect_uri = redirect_uri,
#         scope = scope)
#     return redirect(url)   
    
# def google_authenticate(request):
#     parser = Http()
#     login_failed_url = '/'
#     if 'error' in request.GET or 'code' not in request.GET:
#         return redirect('{loginfailed}'.format(loginfailed = login_failed_url))

#     access_token_uri = 'https://accounts.google.com/o/oauth2/token'
#     redirect_uri = request.build_absolute_uri(reverse('google_auth'))
#     params = urllib.parse.urlencode({
#         'code':request.GET['code'],
#         'redirect_uri':redirect_uri,
#         'client_id':'876151127490-u1kt7kepcffhhqtfpj4snf5cajn7q7o5',
#         'client_secret':'atn-i34pMoMk-ry5V0wu8y4a',
#         'grant_type':'authorization_code'
#     })
#     headers={'content-type':'application/x-www-form-urlencoded'}
#     resp, content = parser.request(access_token_uri, method = 'POST', body = params, headers = headers)
#     token_data = json.loads(content.decode('utf-8'))
#     resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token_data['access_token']))
#     #this gets the google profile!!
#     google_profile = json.loads(content.decode('utf-8'))
#     #log the user in-->
#     #HERE YOU LOG THE USER IN, OR ANYTHING ELSE YOU WANT
#     #THEN REDIRECT TO PROTECTED PAGE
#     return redirect('/')    