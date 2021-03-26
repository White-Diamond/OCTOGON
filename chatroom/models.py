from django.db import models

# Create your models here.
class Chat(models.Model):
    to_uuid = models.CharField(max_length=50)
    from_uuid = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    seen = models.BooleanField()