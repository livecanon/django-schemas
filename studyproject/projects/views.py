from django.shortcuts import render
# from django.http import HttpResponse

projectsList = [
    {'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website' },
    {'id': '2', 'title': 'Portfolio Website', 'description': 'A personal website to write articles and display work' },
    {'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community' }
]

def projects(request):
    # return HttpResponse('Projects page')

    msg = 'Hello, you are on the projects page.'

    context = {
        'msg': msg,
        'projects': projectsList
    }
    
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single-project.html')
