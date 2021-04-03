from django.db import models
import datetime


# This Object is for Threads containing posts
class Thread(models.Model):
    # thread_ID will identify the thread
    thread_ID = models.IntegerField(default=0)
    thread_date = models.DateTimeField(auto_now_add=True)
    threadTopic = models.CharField(max_length=200, default=' ')
    currentPostNumber = models.IntegerField(default=0)
    main_post_id = models.IntegerField(default=0)


# This Object is for Posts contained in threads
class Post(models.Model):
    owning_thread_ID = models.IntegerField(default=0)
    # this allows posts to be identified based on the thread they are contained in
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)  # this should by default add post_set to Thread
    post_ID = models.IntegerField(default=0)
    user_ID = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    main_text = models.TextField()


# This object is for messages
class Message(models.Model):
    # message_ID will identify the message
    message_ID = models.IntegerField(default=0)
    sender_ID = models.IntegerField(default=0)
    recipient_ID = models.IntegerField(default=0)
    message_date = models.DateTimeField(auto_now_add=True)
    main_text = models.TextField()
