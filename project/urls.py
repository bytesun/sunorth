"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = patterns('',
    url(r'^$', 'project.views.home', name='home'),
    url(r'^van/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^registform/', registform, name='registform'),
    url(r'^signin/', signin, name='signin'),
    url(r'^resetpwd/', resetpwd, name='resetpwd'),
)
urlpatterns += i18n_patterns('',
    url(r'^club$', 'project.views.club', name='club'),
    url(r'^blog/', include('blog.urls')),
    url(r'^activity/', include('activity.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^userprofile/', include('userprofile.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^avatar/', include('avatar.urls')),
    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
