from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from .views import (
    LocationViewSet,
    CharacterViewSet,
    EpisodeViewSet,
)


router = routers.DefaultRouter()

router.register(r"locations", LocationViewSet, basename="location")
router.register(r"characters", CharacterViewSet, basename="character")
router.register(r"episodes", EpisodeViewSet, basename="episode")


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="rickandmorty", description="Rick and Morty API (:", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path("", include(router.urls)),
]
