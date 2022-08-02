from django.shortcuts import render
# from django.http import HttpResponse
from .models import Project

projectsList = [
    {'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website' },
    {'id': '2', 'title': 'Portfolio Website', 'description': 'A personal website to write articles and display work' },
    {'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community' }
]

def projects(request):
    # return HttpResponse('Projects page')

    msg = 'Hello, you are on the projects page.'
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {
        'project': project,
    }

    return render(request, 'projects/single-project.html', context)
