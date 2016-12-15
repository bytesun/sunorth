from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^(?P<id>\d+)/$', views.activity_info,name='activity_info'),
    url(r'^list/$', views.list, name='club_list'),
    url(r'^new/$', views.add, name='club_add'),

]