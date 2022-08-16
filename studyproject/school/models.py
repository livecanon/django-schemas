from django.db import models
from django.core.validators import MaxValueValidator


SEMESTER = (
    ("sem1", "sem1"),
    ("sem2", "sem2"),
    ("sem3", "sem3"),
    ("sem4", "sem4"),
)
GENDER = (
    ("male", "male"),
    ("female", "female"),
    ("others", "others"),
)


# --------------------------------------------------------------------------------
# see https://spookylukey.github.io/django-views-the-right-way/thin-views.html
# see https://www.botreetechnologies.com/blog/definitive-guide-for-django-model-managers/


class StudentCustomManager(models.Manager):
    def get_total_students(self):
        return self.all().count()

    def get_students_age_less_or_equal(self, age):
        return self.filter(age__lte=age)

    def get_males(self):
        return self.filter(gender="male")


class StudentCustomQuery(models.QuerySet):
    def male(self):
        return self.filter(gender="male")

    def age_less_or_equal_to(self, age):
        return self.filter(age__lte=age)


class MaleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender="male")


# --------------------------------------------------------------------------------


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    semester = models.CharField(
        choices=SEMESTER, default=SEMESTER[0][0], max_length=100
    )
    enroll_num = models.PositiveIntegerField(
        primary_key=True, validators=[MaxValueValidator(9999999999999)]
    )
    gender = models.CharField(choices=GENDER, default=GENDER[0][0], max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # people = models.Manager() Rename default manager ]
    # objects = models.Manager() If we want to keep default manager, with the same name.

    objects = StudentCustomManager()
    male = MaleManager()

    # We have acces to methods from Manager and Queryset, but we cannot chain them.
    # see https://docs.djangoproject.com/en/3.2/topics/db/managers/#from-queryset
    custom = StudentCustomManager.from_queryset(StudentCustomQuery)()

    # We can chain methods
    # see https://docs.djangoproject.com/en/3.2/topics/db/managers/#creating-a-manager-with-queryset-methods
    query = StudentCustomQuery.as_manager()

    def __str__(self):
        return self.name
