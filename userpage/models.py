from django.db import models

# Create your models here.
class tempUserModel(models.Model):
    userID = models.IntegerField()
    userName = models.CharField(max_length=30)
    