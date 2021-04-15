from django.db import models
from django import forms
from django.db import models

class Course(models.Model):
    name_short = models.CharField(max_length=8)
    name_long = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name_short

class User(models.Model):
    BOOL_VALS = ((True, 'Yes'), (False, 'No'))
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #ENCRYPT THIS!!!!!!!!!!
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30)
    is_instructor = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.username