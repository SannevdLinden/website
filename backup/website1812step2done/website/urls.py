from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from django.conf.urls import include #API

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

    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    #url(r'^snippets/$', views.SnippetList.as_view()), #API
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
