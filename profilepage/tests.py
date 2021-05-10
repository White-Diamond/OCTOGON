from time import sleep
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from profilepage.models import Course, Profile
from selenium import webdriver

class ProfileTestCase(TestCase):
    #setup for tests
    def setUp(self):
        u = User.objects.create(username="ryantest", email="example@example.com", password="password", first_name="Ryant",
                            last_name="Hummelt")
        Course.objects.create(name_short="CMSC 447", name_long="Software Engineering I", description="text goes here")


    def test_User(self):
        driver = webdriver.Chrome()
        #backend test
        user = User.objects.get(username="ryantest")
        user.save()
        profile = Profile.objects.get(user=user)
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(profile.user.first_name, "Ryant")
        self.assertEqual(profile.user.last_name, "Hummelt")
        self.assertEqual(profile.user.email, "example@example.com")
        self.assertEqual(profile.is_instructor, False)
        profile.courses.add(course)
        user.save()
        self.assertEqual(profile.courses.get(name_short="CMSC 447"), course)
        self.assertEqual(profile.courses.get(name_short="CMSC 447").name_long, "Software Engineering I")

        #Front-end tests using selenium
        # driver.get("http://127.0.0.1:8000/accounts/login/")
        # uname_input = driver.find_element_by_id('username')
        # pass_input = driver.find_element_by_id('password')
        # signInButton = driver.find_element_by_id('signIn-action')
        # uname_input.send_keys("ryantest")
        # pass_input.send_keys("password")
        # signInButton.click()
        # sleep(3)
        # self.assertEqual(driver.title(), "User Information")
        # username = driver.find_element_by_id('uname').text
        # self.assertEqual(str(username), "test")
        # fname = driver.find_element_by_id('fname').text
        # self.assertEqual(str(fname), "Ryant")
        # lname = driver.find_element_by_id('lname').text
        # self.assertEqual(str(lname), "Hummelt")
        # email = driver.find_element_by_id('email').text
        # self.assertEqual(str(email), "example@example.com")
        # instr = driver.find_element_by_id('ins').text
        # self.assertEqual(str(instr), "No")


    def test_Course(self):
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(course.name_short, "CMSC 447")
        self.assertEqual(course.name_long, "Software Engineering I")
