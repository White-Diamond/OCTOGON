from django.test import TestCase
from posts.models import Thread, Post, Message
from django.utils import timezone
import datetime

#Test for merge conflicts

class PostsTestCase(TestCase):
    def setUp(self):
        print(int(datetime.datetime.now().timestamp()))
        self.th = Thread.objects.create(
            thread_ID=27,
            thread_date=datetime.datetime(2021, 4, 2, 16, 0, 0, 0),
            threadTopic='Topic Test',
            currentPostNumber=1,
            main_post_id=1
        )
        self.th.save()

        self.po = Post.objects.create(
            thread=self.th,
            post_ID=1,
            user_ID=1,
            post_date=datetime.datetime(2021, 4, 2, 16, 0, 0, 0),
            main_text='Post main text goes here'
        )
        self.po.save()

        self.mess = Message.objects.create(
            recipient_ID=1,
            main_text='Message text goes here'
        )
        self.mess.save()


    def test_Thread(self):
        thread = Thread.objects.get(thread_ID=27)
        #self.assertEqual(
            #int(thread.thread_date.timestamp()),
            #int(datetime.datetime(2021, 4, 2, 16, 0, 0, 0).timestamp()))
            # ^ might have to find a different way to test this
        self.assertEqual(thread.threadTopic, 'Topic Test')
        self.assertEqual(thread.currentPostNumber, 1)
        self.assertEqual(thread.main_post_id, 1)
        self.assertEqual(thread.threadTopic, 'Topic Test')

    def test_Post(self):
        post = Post.objects.get(post_ID=1)
        #self.assertEqual(
            #int(post.post_date.timestamp()),
            #int(datetime.datetime(2021, 4, 2, 4, 16, 0, 0).timestamp()))
            # ^ might have to find a different way to test this
        self.assertEqual(post.thread.thread_ID, 27)
        self.assertEqual(post.user_ID, 1)
        self.assertEqual(post.main_text, 'Post main text goes here')

    def test_Message(self):
        mess = Message.objects.get(message_ID=0)
        #self.assertEqual(
            #int(mess.mess_date.timestamp()),
            #int(datetime.datetime(2021, 4, 2, 4, 16, 0, 0).timestamp()))
            # ^ might have to find a different way to test this
        self.assertEqual(mess.sender_ID, 0)
        self.assertEqual(mess.recipient_ID, 1)
        self.assertEqual(mess.main_text, 'Message text goes here')
