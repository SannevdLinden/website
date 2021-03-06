from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view #corejson

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API') #core json

urlpatterns = [ #all the links to the right webpage
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.data_list2, name='index'), #newnew
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^base/$', views.post_list, name='post_list'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^sessions/$', views.sessions, name='sessions'),

    #newnew
    #url(r'^progress/$', views.progress, name='progress'),

    url(r'^', include(router.urls)), #for the API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view), #corejson

    #neww
    url(r'^post/(?P<pk>\d+)/completed/$', views.post_completed, name='post_completed'),
    url(r'^progress/$', views.data_list, name='data_list'),
    url(r'^settings/$', views.colorsettings, name='colorsettings'),
    url(r'^settings/(?P<pk>\d+)/$', views.color_grey, name='color_grey'),
    url(r'^help/$', views.help_color, name='help_color'),

]
