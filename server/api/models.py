from django.db import models


class DateTimeModel(models.Model):
    """A base model with created and edited datetime fields"""

    class Meta:
        # Abstract base classes are useful when you want to put some common information into a number of other models.
        # You write your base class and put abstract=True in the Meta class.
        # see https://docs.djangoproject.com/en/4.1/topics/db/models/#abstract-base-classes
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Planet(DateTimeModel):
    """A planet i.e. Tatooine"""

    name = models.CharField(max_length=100)
    rotation_period = models.PositiveIntegerField(null=True, blank=True)
    orbital_period = models.PositiveIntegerField(null=True, blank=True)
    diameter = models.PositiveIntegerField(null=True, blank=True)
    climate = models.CharField(max_length=40, null=True, blank=True)
    gravity = models.CharField(max_length=40, null=True, blank=True)
    terrain = models.CharField(max_length=40, null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class People(DateTimeModel):
    """A person i.e. - Luke Skywalker"""

    name = models.CharField(max_length=100)
    height = models.PositiveIntegerField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)
    skin_color = models.CharField(max_length=20, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    birth_year = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=40, null=True, blank=True)
    homeworld = models.ForeignKey(
        Planet, related_name="residents", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class Species(DateTimeModel):
    "A species is a type of alien or person"

    name = models.CharField(max_length=40)
    classification = models.CharField(max_length=40, null=True, blank=True)
    designation = models.CharField(max_length=40, null=True, blank=True)
    average_height = models.PositiveIntegerField(null=True, blank=True)
    skin_colors = models.CharField(max_length=200, null=True, blank=True)
    hair_colors = models.CharField(max_length=200, null=True, blank=True)
    eye_colors = models.CharField(max_length=200, null=True, blank=True)
    average_lifespan = models.PositiveIntegerField(null=True, blank=True)
    homeworld = models.ForeignKey(
        Planet, blank=True, null=True, on_delete=models.SET_NULL
    )
    language = models.CharField(max_length=40, null=True, blank=True)
    people = models.ManyToManyField(People, related_name="species")

    def __str__(self):
        return self.name


class Film(DateTimeModel):
    """A film i.e. The Empire Strikes Back (which is also the best film)"""

    title = models.CharField(max_length=100)
    episode_id = models.PositiveIntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()
    characters = models.ManyToManyField(People, related_name="films", blank=True)
    planets = models.ManyToManyField(Planet, related_name="films", blank=True)
    species = models.ManyToManyField(Species, related_name="films", blank=True)

    def __str__(self):
        return self.title
