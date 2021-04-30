from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Course(models.Model):
    name_short = models.CharField(max_length=8, unique=True)
    name_long = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name_short

class Profile(models.Model):
    # username = models.CharField(max_length=30, unique=True)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100) #ENCRYPT THIS!!!!!!!!!!
    # name_first = models.CharField(max_length=30)
    # name_last = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()