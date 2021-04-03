from django.test import TestCase
from posts.models import Thread
from posts.models import Post
import time

class threadCreation(TestCase):
    
    # Put Threads into the database
    def setUp(self):

        # Make threads and save them to the database
        self.testThread1 = Thread.objects.create(thread_ID=1, threadTopic="Question on HW3 question 2", currentPostNumber=5)
        self.testThread1.save()
        self.testThread2 = Thread.objects.create(thread_ID=2, threadTopic="How to fix \"KENREL POINTER dref\"", currentPostNumber=3)
        self.testThread2.save()

        # make posts for the first thread and save them to the database
        self.testPost1 = Post.objects.create(thread=self.testThread1, owning_thread_ID=1, post_ID=1, main_text="So that from point to point now have you heard The fundamental reasons of this war, Whose great decision hath much blood let forth And more thirsts after.")
        self.testPost1.save()
        self.testPost2 = Post.objects.create(thread=self.testThread1, owning_thread_ID=1, post_ID=2, main_text="Holy seems the quarrel Upon your grace's part; black and fearful On the opposer.")
        self.testPost2.save()
        self.testPost3 = Post.objects.create(thread=self.testThread1, owning_thread_ID=1, post_ID=3, main_text="Therefore we marvel much our cousin France Would in so just a business shut his bosom Against our borrowing prayers.")
        self.testPost3.save()
        self.testPost4 = Post.objects.create(thread=self.testThread1, owning_thread_ID=1, post_ID=4, main_text="Good my lord, The reasons of our state I cannot yield, But like a common and an outward man, That the great figure of a council frames By self-unable motion: therefore dare not Say what I think of it, since I have found Myself in my incertain grounds to fail As often as I guess'd.")
        self.testPost4.save()
        self.testPost5 = Post.objects.create(thread=self.testThread1, owning_thread_ID=1, post_ID=5, main_text="Be it his pleasure.")
        self.testPost5.save()

        # Make posts for the second thread and save them to the database
        self.testPost6 = Post.objects.create(thread=self.testThread1, owning_thread_ID=2, post_ID=1, main_text="Now, what you hear is not a test, I'm rapping to the beat")
        self.testPost6.save()    
        self.testPost7 = Post.objects.create(thread=self.testThread1, owning_thread_ID=2, post_ID=2, main_text="And me, the groove, and my friends are gonna try to move your feet")
        self.testPost7.save()
        self.testPost8 = Post.objects.create(thread=self.testThread1, owning_thread_ID=2, post_ID=3, main_text="You see I am Wonder Mike and I'd like to say hello")
        self.testPost8.save()


    # Test if threads get assigned their chronological id's properly
    def test_getting_Threads(self):
        testThread = Thread.objects.get(thread_ID=1)
        self.assertEqual(testThread.thread_ID, 1)

    # Test if posts belong to the owners of which they are assigned
    def test_Post_Ownership(self):
        tempPost = Post.objects.get(owning_thread_ID=1, post_ID=5)
        self.assertEquals(tempPost.thread.threadTopic, "Question on HW3 question 2")

    # Test if posts are assigned their chronological id's properly
    def test_getting_Posts(self):
        posts_t2 = Post.objects.all()
        latestPost_t2 = posts_t2.filter(owning_thread_ID=2)
        latestPost_t2 = posts_t2.latest('post_date')
        self.assertEqual(latestPost_t2.post_ID, 3)

    


        