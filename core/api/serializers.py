from rest_framework import serializers
from .models import Location, Character, Episode


class LocationSerializer(serializers.ModelSerializer):
    dimension = serializers.CharField(required=False)

    class Meta:
        model = Location
        fields = [
            "id",
            "createdAt",
            "editedAt",
            "name",
            "type",
            "dimension",
        ]


class CharacterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=False)

    class Meta:
        model = Character
        fields = [
            "id",
            "createdAt",
            "editedAt",
            "name",
            "status",
            "gender",
            "species",
            "type",
            "origin",
            "image",
            "episodes",
        ]


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"
