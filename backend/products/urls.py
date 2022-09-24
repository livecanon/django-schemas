from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateProductAPIView.as_view()),
    path("<int:pk>", views.RetrieveUpdateDestroyAPIView.as_view()),
]
