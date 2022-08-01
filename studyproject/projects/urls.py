from multiprocessing.spawn import import_main_path
from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
]
