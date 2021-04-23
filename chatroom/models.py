from django.db import models

# Create your models here.
class Message(models.Model):
    to_id = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50) 
    message = models.CharField(max_length=5000)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)