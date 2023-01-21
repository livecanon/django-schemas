from django.contrib import admin
from .models import Planet, People, Species, Film


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("name", "diameter", "population", "climate")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(People)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("name", "height", "mass", "birth_year")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Species)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("name", "classification", "average_height", "average_lifespan")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Film)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "producer", "director")
    search_fields = ("title",)
    ordering = ("id",)
