from django.db import models

# Create your models here.
class Chat(models.Model):
    to_id = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50)

class Message():
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    seen = models.BooleanField()
    created_at = models.DateTimeField()
    count = models.IntegerField()
