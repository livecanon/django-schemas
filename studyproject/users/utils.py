from django.db.models import Q
from .models import Profile, Skill


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET['search_query']
    
    skills = Skill.objects.filter(name__icontains=search_query)

    # When we use Q, we can do | or &
    # see https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query
