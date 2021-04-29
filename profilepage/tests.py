from django.test import TestCase
from profilepage.models import Course, Profile
from selenium import webdriver

class UserTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(username="warsh1", email="example@example.com", password="password", name_first="James",
                            name_last="Warshaw", is_instructor=False)
        Course.objects.create(name_short="CMSC 447", name_long="Software Engineering I")
        Profile.objects.create(username="test", email="test@umbc.edu", password="password", name_first="John",
                            name_last="Doe", is_instructor=False)


    def test_User(self):
        driver = webdriver.Chrome()
        user = Profile.objects.get(username="warsh1")
        user.save()
        course = Course.objects.get(name_short="CMSC 447")
        course.save()
        self.assertEqual(user.name_first, "James")
        self.assertEqual(user.name_last, "Warshaw")
        self.assertEqual(user.is_instructor, False)
        user.courses.add(course)
        user.save()
        self.assertEqual(user.courses.get(id=1), course)
        self.assertEqual(user.courses.get(id=1).name_long, "Software Engineering I")

        #Front-end tests using selenium
        #Tests work if database entry is added automatically
        #They fail for now because we have not set up a way to populate the profile database,
        #Causing the page to crash
        # driver.get("http://127.0.0.1:8000/")
        # self.assertEqual(driver.title, "User Information")
        # username = driver.find_element_by_id('uname').text
        # self.assertEqual(str(username), "test")
        # name = driver.find_element_by_id('name').text
        # self.assertEqual(str(name), "John Doe")
        # email = driver.find_element_by_id('email').text
        # self.assertEqual(str(email), "test@umbc.edu")
        # instr = driver.find_element_by_id('ins').text
        # self.assertEqual(str(instr), "No")


    def test_Course(self):
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(course.name_short, "CMSC 447")
        self.assertEqual(course.name_long, "Software Engineering I")
