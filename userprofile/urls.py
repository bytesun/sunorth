from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.userprofile,name='userprofile'),

]