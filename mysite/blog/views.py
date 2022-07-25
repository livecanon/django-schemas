from django.shortcuts import redirect, render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts.html', context=context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context=context)
