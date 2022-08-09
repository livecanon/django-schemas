from django.db.models import Q
from .models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projects, results):
    # see https://docs.djangoproject.com/en/3.2/topics/pagination/
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    
    custom_range = range(left_index, right_index)

    return custom_range, projects


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
