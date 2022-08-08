from django.db.models import Q
from .models import Project, Tag


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET['search_query']
    
    tags = Tag.objects.filter(name__icontains=search_query)

    # see https://docs.djangoproject.com/en/3.2/topics/db/queries/#lookups-that-span-relationships
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects, search_query
