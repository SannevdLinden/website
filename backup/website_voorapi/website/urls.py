from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^base/$', views.post_list, name='post_list'),
    url(r'^delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^sessions/$', views.sessions, name='sessions'),
    url(r'^progress/$', views.progress, name='progress'),
    #url(r'^base/$', views.base, name='base'), #for adding other page
]
