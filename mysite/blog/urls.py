from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name='post_list'),
    path("<int:id>/", views.post_detail, name='post_detail'),
]
