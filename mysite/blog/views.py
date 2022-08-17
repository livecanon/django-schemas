from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView
from django.conf import settings

from .forms import EmailPostForm, CommentForm
from .models import Post
from taggit.models import Tag


class PostListView(ListView):
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

    # get_queryset() doesn't take additional parameters as input.
    # But you can use self.kwargs object to access URL parameters.
    # Something like this: pk = self.kwargs['pk']
    def get_queryset(self):
        if self.kwargs.get("tag_slug"):
            tag = get_object_or_404(Tag, slug=self.kwargs.get("tag_slug"))
            # see https://docs.djangoproject.com/en/4.1/ref/models/querysets/#in
            return Post.published.filter(tags__in=[tag])
        else:
            return Post.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get("tag_slug"):
            context["tag"] = self.kwargs.get("tag_slug")
        return context


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comments = post.comments.filter(active=True)

    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    context = {"post": post, "comments": comments, "form": form}

    return render(request, "blog/post/detail.html", context=context)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        # see https://docs.djangoproject.com/en/3.2/topics/forms/#field-data
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) encourages you to read "{}"'.format(
                cd["name"], cd["email"], post.title
            )
            message = "Read {} on website {}\n\n Comment was added by {}: {}".format(
                post.title, post_url, cd["name"], cd["comments"]
            )
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()

    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )
