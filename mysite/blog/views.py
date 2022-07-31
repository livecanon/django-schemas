from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class PostList(ListView):
    # model = Post
    paginate_by = 3
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='published').order_by('-last_modified')


class PostDetail(DetailView):
    # model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    # see https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/
    queryset = Post.objects.filter(status='published')


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create.html'
    form_class = PostForm
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 'published'
        return super().form_valid(form)
