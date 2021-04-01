from django.db import models

# Create your models here.
class tempUserModel(models.Model):
    userID = models.IntegetField()
    userName = models.CharField()
    