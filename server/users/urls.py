from django.urls import path
from .views import UserCreate

app_name = "users"

urlpatterns = [
    path("create/", UserCreate.as_view(), name="create_user"),
]
