from django.shortcuts import render
from django.utils import timezone
from .models import Post, Event #ADDED
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, EventForm #ADDED
from django.shortcuts import redirect
#ADDED BElOW
import datetime
import calendar
from django.urls import reverse
from django.utils.safestring import mark_safe
from .utils import EventCalendar

# From here added by Lars----------------------------------------------------------------

from django.contrib.auth import login, authenticate
from website.forms import SignUpForm
from django.shortcuts import render, redirect #render also mentioned above
from django.contrib.auth.decorators import login_required

# Till here added by Lars----------------------------------------------------------------

from .forms import BlogForm, CommentForm #Sebastiaan
from .models import Blog, Comment, Flagged #Sebastiaan
from django.shortcuts import render_to_response#Sebastiaan
from django.template import RequestContext#Sebastiaan
from django.http import HttpResponseRedirect#Sebastiaan
from django.core.urlresolvers import reverse#Sebastiaan
from django.contrib.auth.decorators import login_required #Sebastiaan

#API
from website.models import Post
from website.serializers import SnippetSerializer, SessionSerializer #ADDED
from rest_framework import generics
from django.contrib.auth.models import User
from website.serializers import UserSerializer
from rest_framework import permissions
from website.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.http import Http404

#NEWNEW
from .models import Depthdata
from .models import Bpdata
from .models import Frdata
from .models import Speeddata
from .models import Colorsetting

def index(request): #for adding other page
    return render(request, 'website/index.html', {})

def base(request): #for adding other page
    return render(request, 'website/base.html', {})

#ADDED

def sessions_listx(request):
    events = Event.objects.filter(day__lte=timezone.now()).order_by('start_time')
    return render(request, 'website/sessions.html', {'events': events})

def sessions_list(request, extra_context=None):
    after_day = request.GET.get('day__gte', None)
    extra_context = extra_context or {}

    if not after_day:
        d = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
        except:
            d = datetime.date.today()

    previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
    previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
								   day=1)  # find first day of previous month

    last_day = calendar.monthrange(d.year, d.month)
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month,
							   day=1)  # find first day of next month

    extra_context['previous_month'] = reverse('website:sessions_list') + '?day__gte=' + str(previous_month)
    extra_context['next_month'] = reverse('website:sessions_list') + '?day__gte=' + str(next_month)

    cal = EventCalendar()
    html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
    extra_context['cal'] = mark_safe(html_calendar)
    return render(request, 'website/sessions.html', extra_context)

def session_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'website/session_detail.html', {'event': event})

def session_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('/sessions/')
    else:
        form = EventForm()
    return render(request, 'website/session_edit.html', {'form': form})

def session_edit(request, pk): #to make a new session
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('/sessions/')
    else:
        form = EventForm(instance=event)
    return render(request, 'website/session_edit.html', {'form': form})

def session_delete(request,pk): #to delete a session
    u = Event.objects.get(pk=pk).delete()
    return redirect('/sessions/')
    return render(request, 'website/sessions.html', {})
#END ADDED

def progress(request): #for adding other page
    return render(request, 'website/progress.html', {})

def post_list(request): #for displaying the todo's in a table
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/post_list.html', {'posts': posts})

def post_detail(request, pk): #for dislaying a detailed to do
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})

def post_new(request): #to make a new todo item
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.title = 'notcomplete'
            #post.number = 0
            post.save()
            return redirect('/base/')
    else:
        form = PostForm()
    return render(request, 'website/post_edit.html', {'form': form})

def post_edit(request, pk): #to make a new to do item
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            #post.number = 0
            post.save()
            return redirect('/base/')
    else:
        form = PostForm(instance=post)
    return render(request, 'website/post_edit.html', {'form': form})

def post_delete(request,pk): #to delete a todo item
    u = Post.objects.get(pk=pk).delete()
    return redirect('/base/')
    return render(request, 'website/base.html', {})

# From here added by Lars----------------------------------------------------------------

def profile(request): #for adding other page
    return render(request, 'website/profile.html', {})

def profile_change(request): #for adding other page
    return render(request, 'website/profile_change.html', {})

@login_required
def index(request):
    return render(request, 'website/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

# Till here added by Lars----------------------------------------------------------------

def blog_new(request):   #Sebastiaan
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():

            blog = form.save(commit=False)
            blog.author = request.user
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
        blogs = Blog.objects.all()
    return render(request, 'website/blog_edit.html', {'blogs':blogs, 'form': form}) #'documents': documents,
        # Handle file upload

def blog_detail(request, pk): #Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return render(request, 'website/blog_detail.html', {'blog': blog, 'blogs': blogs, 'flaggeds':flaggeds})

def blog_edit(request, pk): #Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
        blogs = Blog.objects.all()
        #documents = Document.objects.all()
    return render(request, 'website/blog_edit.html', {'blogs': blogs, 'form': form})  #'documents': documents,

def blog_list(request):   #Sebastiaan
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return render(request, 'website/blog_list.html', {'blogs': blogs, 'flaggeds':flaggeds})

def blog_remove(request, pk):#Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_list')

def blog_flagdetail(request, pk):#Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    blog.flags = blog.flags + 1;
    blog.save()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    new_like = Flagged()
    new_like.blog = blog
    new_like.username = request.user
    new_like.save()
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return redirect('blog_detail', pk=blog.pk)
    #blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'website/blog_detail.html', {'blog': blog})

def blog_flaglist(request, pk):#Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    blog.flags = blog.flags + 1;
    blog.save()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    new_like = Flagged()
    new_like.blog = blog
    new_like.username = request.user
    new_like.save()
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return redirect('blog_list')
    #return render(request, 'website/blog_list.html', {'blogs': blogs})

def blog_flaglist_remove(request, pk):#Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    flags = Flagged.objects.all()
    for flag in flags:
        if blog.pk == flag.blog.pk and flag.username == request.user:
            flag.delete()
    blog.flags = blog.flags - 1;
    blog.save()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return redirect('blog_list')

def blog_flagdetail_remove(request, pk):#Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    flags = Flagged.objects.all()
    for flag in flags:
        if blog.pk == flag.blog.pk and flag.username == request.user:
            flag.delete()
    blog.flags = blog.flags - 1;
    blog.save()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-flags')
    flaggeds = Flagged.objects.all()
    flaggeds = flaggeds[::-1]
    return redirect('blog_detail', pk=blog.pk)
        #return render(request, 'website/blog_list.html', {'blogs': blogs})



def add_comment_to_blog(request, pk): #Sebastiaan
    blog = get_object_or_404(Blog, pk=pk)
    #commenttarget = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            #comment.target = None
            comment.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, 'website/add_comment_to_blog.html', {'form': form})

def add_comment_to_comment(request, pk): #Sebastiaan
    commenttarget = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = commenttarget.blog
            comment.author = request.user
            comment.target = commenttarget.author
            comment.save()
            return redirect('blog_detail', pk=comment.blog.pk)
    else:
        form = CommentForm()
    return render(request, 'website/add_comment_to_blog.html', {'form': form})

def comment_remove(request, pk): #Sebastiaan
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog_detail', pk=comment.blog.pk)

#NEWWWWWW
def post_completed(request, pk): #to complete to do item
    u = Post.objects.get(pk=pk)
    if u.title == 'notcomplete':
        u.title = 'complete'
    elif u.title == 'complete':
        u.title = 'notcomplete'
    u.save()
    return redirect('/base/')
    return render(request, 'website/base.html', {})

def data_list(request): #for displaying the todo's in a table
    depthdata = Depthdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    bpdata = Bpdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    frdata = Frdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    sdata = Speeddata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    color = get_object_or_404(Colorsetting)
    return render(request, 'website/data_list.html', {'ddata': depthdata, 'bpdata': bpdata, 'frdata': frdata, 'sdata': sdata, 'color': color})

def data_list2(request): #for displaying the todo's in a table
    depthdata = Depthdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[9:10]
    bpdata = Bpdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[9:10]
    frdata = Frdata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[9:10]
    sdata = Speeddata.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[9:10]
    color = get_object_or_404(Colorsetting)
    return render(request, 'website/data_list2.html', {'ddata': depthdata, 'bpdata': bpdata, 'frdata': frdata, 'sdata': sdata, 'color': color})

def settings(request): #for adding other page
    return render(request, 'website/settings.html', {})

def help_color(request): #for adding other page
    color = get_object_or_404(Colorsetting)
    return render(request, 'website/help_color.html', {'color': color})

def colorsettings(request): #for displaying the todo's in a table
    #color = Colorsetting.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    color = get_object_or_404(Colorsetting)
    return render(request, 'website/colorsettings.html', {'color': color})

def color_grey(request, pk): #to complete to do item
    grey = get_object_or_404(Colorsetting, pk=pk)
    if grey.title == 'c':
        grey.title = 'g'
    elif grey.title == 'g':
        grey.title = 'c'
    grey.save()
    return redirect('/settings/')
    return render(request, 'website/settings.html', {})

class SnippetViewSet(viewsets.ModelViewSet): #for the API to make sure people can get the todo data
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlighted(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet): #for the API to make sure teh user data is available
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

#ADDED
class SessionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Event.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


@api_view(['GET']) #for the API to display everything
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format) #ADDED
    })
