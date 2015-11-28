from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/$', views.photo_upload, name='photo_upload'),
    url(r'^list/$', views.photo_list, name='photo_list'),
]