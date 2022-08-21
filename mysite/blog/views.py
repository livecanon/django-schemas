from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/posts.html", context=context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "blog/post.html", context=context)


@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        response = redirect("/blog")
        return response

    return render(request, "blog/create.html")
