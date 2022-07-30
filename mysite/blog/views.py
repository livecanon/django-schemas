from .models import Post
from django.views.generic import ListView, DeleteView

class PostList(ListView):
    # model = Post
    paginate_by = 3
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='published').order_by('-last_modified')


class PostDetail(DeleteView):
    # model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    # see https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/
    queryset = Post.objects.filter(status='published')

