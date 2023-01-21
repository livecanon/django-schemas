from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from .views import (
    PlanetViewSet,
    PeopleViewSet,
    SpeciesViewSet,
    FilmViewSet,
)


router = routers.DefaultRouter()

router.register(r"planets", PlanetViewSet, basename="planet")
router.register(r"people", PeopleViewSet, basename="people")
router.register(r"species", SpeciesViewSet, basename="species")
router.register(r"films", FilmViewSet, basename="film")


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="starwars", description="starwars API …", version="1.0.0"
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
