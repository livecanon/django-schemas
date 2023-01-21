from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Planet, People, Species, Film
from .serializers import (
    PlanetSerializer,
    PeopleSerializer,
    SpeciesSerializer,
    FilmSerializer,
)


class PlanetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Planet.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PlanetSerializer


class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = People.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PeopleSerializer


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = SpeciesSerializer


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = FilmSerializer
