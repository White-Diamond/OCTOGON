from django.db import models

# Create your models here.
class Chat(models.Model):
    to_id = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50) 

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

