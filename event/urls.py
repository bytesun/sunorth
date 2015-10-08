from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.event_info,name='event_info'),
    url(r'^list/$', views.event_list, name='event_list'),
    url(r'^new/$', views.event_new, name='event_new'),
    url(r'^edit/(?P<id>\d+)/$', views.event_edit, name='event_edit'),
]