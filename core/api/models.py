from django.db import models


class DateTimeModel(models.Model):
    """A base model with created and edited datetime fields"""

    class Meta:
        abstract = True

    createdAt = models.DateTimeField(auto_now_add=True)
    editedAt = models.DateTimeField(auto_now=True)


class Location(DateTimeModel):
    name = models.CharField(
        max_length=250,
        unique=True,
    )
    type = models.CharField(
        max_length=50,
        help_text="The type of the location, e.g Plant.",
    )
    dimension = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The dimension in which the location is located.",
    )

    def __str__(self):
        return self.name


class Character(DateTimeModel):

    STATUS = (
        ("alive", "Alive"),
        ("dead", "Dead"),
        ("unknown", "unknown"),
    )

    GENDER = (
        ("male", "Male"),
        ("female", "Female"),
        ("genderless", "Genderless"),
        ("unknown", "unknown"),
    )

    name = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS)
    gender = models.CharField(max_length=20, choices=GENDER)
    species = models.CharField(max_length=50)
    type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="The type or subspecies of the character",
    )
    origin = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    image = models.ImageField(upload_to="characters/avatar/")

    def __str__(self):
        return self.name


class Episode(DateTimeModel):
    title = models.CharField(max_length=250)
    release = models.DateField()
    season = models.PositiveSmallIntegerField()
    episode = models.PositiveSmallIntegerField()
    characters = models.ManyToManyField(Character, related_name="episodes")

    def __str__(self):
        return self.title
