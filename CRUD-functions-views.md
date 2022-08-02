# CRUD

### 1. Create

> views.py
```
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)
```

> urls.py
```
    path('create-project/', views.createProject, name='create-project'),
```

> forms.py
```
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
```

> HTML
```
{% extends 'main.html' %}

{% block content %}
    <h1>Project form</h1>

    <form method='POST'>
        {% csrf_token %}
        {% for field in form %}
            {{field.label}}
            {{field}}
        {% endfor %}
        <input type='submit' />
    </form>
{% endblock content %}
```
---

### 2. Read

> views
```
def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {
        'project': project,
    }

    return render(request, 'projects/single-project.html', context)

```

> urls
```
    path('project/<str:pk>/', views.project, name='project'),
```

> HTML
```
{% extends 'main.html' %}

{% block content %}
    <h1>Single Project</h1>
    <hr/>
    <h2>{{project.title}}</h2>
    <hr/>
        <ul>
            {% for tag in project.tags.all %}
                <li>{{tag.name}}</li>
            {% endfor %}
        </ul>
    <hr/>
    <h3>{{project.description}}</h3>
{% endblock content %}

```
---
3. Update

> views
```
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    # see https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)
```

> urls
```
    path('update-project/<str:pk>', views.updateProject, name='update-project'),
```

> HTML (same as CREATE)
```
{% extends 'main.html' %}

{% block content %}
    <h1>Project form</h1>

    <form method='POST'>
        {% csrf_token %}
        {% for field in form %}
            {{field.label}}
            {{field}}
        {% endfor %}
        <input type='submit' />
    </form>
{% endblock content %}
```

---
4. Delete

> views
```
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context=context)
```

> urls
```
    path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
```

> HTML
```
{% extends 'main.html' %}

{% block content %}

<form method='POST'>
    {% csrf_token %}
    <p>Are you sure you want to delete "{{object}}"?</p>
    <a href="{% url 'projects' %}">Go back</a>
    <input type='submit' value='Confirm' />
</form>

{% endblock content %}
```