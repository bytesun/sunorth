from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.book_info,name='book_info'),
    url(r'^new/$', views.book_new, name='book_new'),
    url(r'^edit/(?P<id>\d+)/$', views.book_edit, name='book_edit'),
    url(r'^list/$', views.book_list, name='book_list'),
    url(r'^comment/(?P<bookid>\d+)/$', views.comment_new, name='book_comment_new'),
]