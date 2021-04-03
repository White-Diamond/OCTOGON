from django.test import TestCase
from user_profile_db.models import Course, User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="warsh1", email="example@example.com", password="password", name_first="James", name_last="Warshaw", is_instructor=False)
        Course.objects.create(name_short="CMSC 447", name_long="Software Engineering I")
    def test_User(self):
        user = User.objects.get(username="warsh1")
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
    def test_Course(self):
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(course.name_short, "CMSC 447")
        self.assertEqual(course.name_long, "Software Engineering I")