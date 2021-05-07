from django.db import models

# Create your models here.
class UserList(models.Model):
    active_user = models.CharField(max_length=50)
    other_user = models.CharField(max_length=50) 
    has_notification = models.BooleanField(default=False)

class Message(models.Model):
    to_id = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50) 
    message = models.CharField(max_length=5000)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)