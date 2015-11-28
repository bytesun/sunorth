from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.activity_info,name='activity_info'),
    url(r'^list/$', views.activity_list, name='activity_list'),
    url(r'^new/$', views.activity_new, name='activity_new'),
    url(r'^edit/(?P<id>\d+)/$', views.activity_edit, name='activity_edit'),
    url(r'^comment/(?P<activityid>\d+)/$', views.comment_new, name='activity_comment_new'),
]