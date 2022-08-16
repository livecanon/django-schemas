# Generated by Django 3.2.14 on 2022-08-16 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('semester', models.CharField(choices=[('sem1', 'sem1'), ('sem2', 'sem2'), ('sem3', 'sem3'), ('sem4', 'sem4')], default='sem1', max_length=100)),
                ('enroll_num', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999999)])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='male', max_length=100)),
                ('registered_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
