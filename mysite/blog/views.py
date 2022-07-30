from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostList(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context=context)
