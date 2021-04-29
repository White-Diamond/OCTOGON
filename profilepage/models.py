from django.db import models
from django import forms
from django.db import models

from django.contrib.auth.models import User

class Course(models.Model):
    name_short = models.CharField(max_length=8)
    name_long = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name_short

# This user model needs to extend the default user model via a OneToOne Field

class Profile(models.Model):

    duser = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30)
    is_instructor = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name_first
