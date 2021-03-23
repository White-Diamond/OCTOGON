from django.db import models

# Create your models here.
class Chat(models.Model):
    sender_uuid = models.CharField(max_length=50)
    receiver_uuid = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    seen = models.BooleanField()