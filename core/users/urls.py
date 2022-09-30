from django.urls import path
from .views import UserCreate, BlacklistTokenUpdateView

app_name = "users"

urlpatterns = [
    path("create/", UserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),
]
