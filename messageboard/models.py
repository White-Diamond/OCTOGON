from django.db import models

# temporary model for testing display of threads
class tempThreadModel (models.Model):
    threadTopic = models.IntegerField()
    main_text = models.TextField()
