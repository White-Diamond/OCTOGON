from django.db import models

# Create your models here.
class tempThreadModel (models.Model):
    threadID = models,IntegerField()
    main_text = models.TextField()
