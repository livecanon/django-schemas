from django.contrib import admin
from .models import Location, Character, Episode


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "type", "dimension")
    readonly_fields = ("id",)
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "gender", "status", "species")
    readonly_fields = ("id",)
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["title", "season", "episode", "release"]
    search_fields = ("title",)
    list_filter = ("season",)
    filter_horizontal = ("characters",)
