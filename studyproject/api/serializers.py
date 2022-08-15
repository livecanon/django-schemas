from rest_framework import serializers
from users.models import Profile
from projects.models import Project, Tag, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    # see https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    #  seehttps://www.django-rest-framework.org/community/3.0-announcement/#optional-argument-to-serializermethodfield
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    # It has to start with 'get_' prefix
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
