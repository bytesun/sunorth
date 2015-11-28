from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.blog_info,name='blog_info'),
    url(r'^new/$', views.blog_new, name='blog_new'),
    url(r'^edit/(?P<id>\d+)/$', views.blog_edit, name='blog_edit'),
    url(r'^list/$', views.blog_list, name='blog_list'),
    url(r'^comment/(?P<blogid>\d+)/$', views.comment_new, name='blog_comment_new'),
]