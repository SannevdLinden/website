from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

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
