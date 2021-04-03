from django.db import models
import datetime


class Thread(models.Model):
    thread_ID = models.IntegerField(default=0)
    thread_date = models.DateTimeField(auto_now_add=True)
    threadTopic = models.CharField(max_length=200, default=' ')
    currentPostNumber = models.IntegerField(default=0)
    main_post_id = models.IntegerField(default=0)


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE) #this should by default add post_set to Thread
    owning_thread_ID = models.IntegerField(default=0)
    post_ID = models.IntegerField(default=0)
    user_ID = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    main_text = models.TextField()


class Message(models.Model):
    message_ID = models.IntegerField(default=0)
    sender_ID = models.IntegerField(default=0)
    recipient_ID = models.IntegerField(default=0)
    message_date = models.DateTimeField(auto_now_add=True)
    main_text = models.TextField()
