from django.db.models import Count
from django import template
from ..models import Post

register = template.Library()

# --- Note ---
# Po dodaniu nowego modułu znaczników konieczne jest
# ponowne uruchomienie serwera programistycznego.


# see https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/#simple-tags
# simple_tag() - przetworzenie danych i zwrot ciągu tekstowego
@register.simple_tag
def total_posts():
    return Post.published.count()


# see https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/#howto-custom-template-tags-inclusion-tags
# inclusion_tag() - przetworzenie danych i zwrot wygenerowanego szablonu
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    # see https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]
