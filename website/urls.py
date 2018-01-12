from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view #corejson

# From here added by Lars----------------------------------------------------------------

from django.contrib.auth import views as auth_views
from website import views as core_views

# Till here added by Lars----------------------------------------------------------------

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'events', views.SessionViewSet) #ADDED

schema_view = get_schema_view(title='Pastebin API') #core json

urlpatterns = [ #all the links to the right webpage
    url(r'^$', views.data_list2, name='index'), #newnew
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^base/$', views.post_list, name='post_list'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^sessions/$', views.sessions_list, name='sessions_list'), #ADDED
    url(r'^([0-9]{4})/$', views.sessions_list, name='sessions_list'), #ADDED
    url(r'^sessions/event/(?P<pk>\d+)/$', views.session_detail, name='session_detail'), #ADDED
    url(r'^event/new/$', views.session_new, name='session_new'), #ADDED
    url(r'^event/(?P<pk>\d+)/edit/$', views.session_edit, name='session_edit'), #ADDED
    url(r'^event/delete/(?P<pk>\d+)/$', views.session_delete, name='session_delete'), #ADDED
    #url(r'^progress/$', views.progress, name='progress'),
    url(r'^', include(router.urls)), #for the API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view), #corejson
    # From here added by Lars----------------------------------------------------------------
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile_change/$', views.profile_change, name='profile_change'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    # Till here added by Lars----------------------------------------------------------------
    url(r'^blog$', views.blog_list, name='home'), #Sebastiaan
    url(r'^blog$', views.blog_list, name='blog_list'), #Sebastiaan
    url(r'^blog/(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),#Sebastiaan
    url(r'^blog/new/$', views.blog_new, name='blog_new'),#Sebastiaan
    url(r'^blog/(?P<pk>\d+)/edit/$', views.blog_edit, name='blog_edit'),#Sebastiaan
    url(r'^blog/(?P<pk>\d+)/remove/$', views.blog_remove, name='blog_remove'), #Sebastiaan
    url(r'^blog/(?P<pk>\d+)/ $', views.blog_flagdetail, name='blog_flagdetail'), #Sebastiaan
    url(r'^blog/(?P<pk>\d+)/flaglist$', views.blog_flaglist, name='blog_flaglist'), #Sebastiaan
    url(r'^blog/(?P<pk>\d+)/flaglist_remove$', views.blog_flaglist_remove, name='blog_flaglist_remove'), #SebastiaanNEW
    url(r'^blog/(?P<pk>\d+)/flagdetail_remove$', views.blog_flagdetail_remove, name='blog_flagdetail_remove'), #SebastiaanNEW
    url(r'^blog/(?P<pk>\d+)/comment/$', views.add_comment_to_blog, name='add_comment_to_blog'), #Sebastiaan
    url(r'^blog/(?P<pk>\d+)/comment /$', views.add_comment_to_comment, name='add_comment_to_comment'), #Sebastiaan
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'), #Sebastiaan
    #neww
    url(r'^post/(?P<pk>\d+)/completed/$', views.post_completed, name='post_completed'),
    url(r'^progress/$', views.data_list, name='data_list'),
    url(r'^settings/$', views.colorsettings, name='colorsettings'),
    url(r'^settings/(?P<pk>\d+)/$', views.color_grey, name='color_grey'),
    url(r'^help/$', views.help_color, name='help_color'),

]
