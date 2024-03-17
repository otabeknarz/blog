from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'post/home.html')


def posts(request):
    query = None
    posts = Post.objects.filter(status=Post.Publish.PUBLISHED)
    if 'search' in request.GET:
        query = request.GET['search']
        posts = posts.filter(title__icontains=query)

    return render(request, 'post/posts.html', {'posts': posts, 'query': query})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Publish.PUBLISHED)
    return render(request, 'post/post.html', {'post': post})