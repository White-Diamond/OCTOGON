from django.db import models

# temporary model for testing display of threads
class tempThreadModel (models.Model):
    threadID = models.IntegerField()
    main_text = models.TextField()
