from django.test import TestCase
from user_profile_db.models import Course, Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="warsh1", first_name="James", last_name="Warshaw", email="example@example.com", password="password")
        # Profile.objects.create(user=user_base, is_instructor=False)
        # Profile.objects.create(username="warsh2", email="example@example2.com", password="password", name_first="James2", name_last="Warshaw2", is_instructor=False)
        # Profile.objects.create(username="warsh3", email="example@example3.com", password="password", name_first="James3", name_last="Warshaw3", is_instructor=False)
        # Profile.objects.create(username="warsh4", email="example@example4.com", password="password", name_first="James4", name_last="Warshaw4", is_instructor=False)
        Course.objects.create(name_short="CMSC 447", name_long="Software Engineering I")
        Course.objects.create(name_short="CMSC 448", name_long="Software Engineering II")
        Course.objects.create(name_short="CMSC 449", name_long="Software Engineering III")
        Course.objects.create(name_short="CMSC 450", name_long="Software Engineering IV")
    def test_Profile(self):
        user = User.objects.get(username="warsh1")
        # profile.save()
        course = Course.objects.get(name_short="CMSC 447")
        # course.save()
        self.assertEqual(user.first_name, "James")
        self.assertEqual(user.last_name, "Warshaw")
        self.assertEqual(user.profile.is_instructor, False)
        user.profile.courses.add(course)
        # profile.save()
        self.assertEqual(user.profile.courses.get(id=1), course)
        self.assertEqual(user.profile.courses.get(id=1).name_long, "Software Engineering I")
    def test_Course(self):
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(course.name_short, "CMSC 447")
        self.assertEqual(course.name_long, "Software Engineering I")
    
    #THIS IS PURELY FOR PERSONAL TESTING REASONS
    def test_Test(self):
        user = User.objects.get(username="warsh1")
        course1 = Course.objects.get(name_short="CMSC 447")
        course2 = Course.objects.get(name_short="CMSC 448")
        course3 = Course.objects.get(name_short="CMSC 449")
        course4 = Course.objects.get(name_short="CMSC 450")
        user.profile.courses.add(course1)
        user.profile.courses.add(course2)
        user.profile.courses.add(course3)
        print("\nclasses in user")
        for foo in user.profile.courses.all():
            print(foo.name_long)
        print("profiles in class 2")
        for bar in course2.profile_set.all():
            print(bar)
        print("profiles in class 1")
        for baz in course1.profile_set.all():
            print(baz)
        print("all courses")
        for beef in Course.objects.all():
            print(beef)
        print(user.profile.courses.filter(name_short=course2.name_short).exists())
        print(Course.objects.difference(user.profile.courses.all()))