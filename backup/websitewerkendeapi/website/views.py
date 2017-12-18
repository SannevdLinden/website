from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

#from website.models import Snippet #API
from website.models import Post
from website.serializers import SnippetSerializer #API
from rest_framework import generics

from django.contrib.auth.models import User #step4
from website.serializers import UserSerializer
from rest_framework import permissions
from website.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view #step5
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


def index(request): #for adding other page
    return render(request, 'website/index.html', {})

def base(request): #for adding other page
    return render(request, 'website/base.html', {})

def sessions(request): #for adding other page
    return render(request, 'website/sessions.html', {})

def progress(request): #for adding other page
    return render(request, 'website/progress.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})

def post_new(request):
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

def post_edit(request, pk):
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

def post_delete(request,pk):
    u = Post.objects.get(pk=pk).delete()
    return redirect('/base/')
    return render(request, 'website/base.html', {})

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    #queryset = Snippet.objects.all()
    queryset = Post.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET']) #step5
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
