from django.test import TestCase
from posts.models import Thread, Post
from django.utils import timezone
import datetime


class PostsTestCase(TestCase):
    def setUp(self):
        self.th = Thread.objects.create(
            thread_ID=1,
            thread_date=datetime.date.today(),
            threadTopic='Topic Test',
            currentPostNumber=1,
            main_post_id=1
        )
        self.th.save()
        self.po = Post.objects.create(
            thread=self.th,
            post_ID=1,
            user_ID=1,
            post_date=timezone.now(),
            main_text='Post main text goes here'
        )
        self.po.save()


    def test_Thread(self):
        thread = Thread.objects.get(thread_ID=1)
        post = Post.objects.get(post_ID=1)
        #self.assertEqual(thread.thread_date, datetime.date.today()) <-might have to find a different way to test this
        self.assertEqual(thread.threadTopic, 'Topic Test')
        self.assertEqual(thread.currentPostNumber, 1)
        self.assertEqual(thread.main_post_id, 1)

    def test_Post(self):
        post = Post.objects.get(thread_ID=1)
        post = Post.objects.get(post_ID=1)
        #self.assertEqual(post.post_date, datetime.date.today()) <-might have to find a different way to test this
        self.assertEqual(post.thread, setUp.th)
        self.assertEqual(post.user_ID, 1)
        self.assertEqual(post.main_post_id, 1)