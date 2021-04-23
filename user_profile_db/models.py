from django.db import models

class Course(models.Model):
    name_short = models.CharField(max_length=8, unique=True)
    name_long = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name_short

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #ENCRYPT THIS!!!!!!!!!!
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30)
    is_instructor = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.username