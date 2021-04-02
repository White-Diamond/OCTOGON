# Project Octogon<br>

*******************************************************************************************
TEST INSTRUCTIONS (Django native test suite):
*******************************************************************************************
I have 3 test classes. Each class is in test.py in the chatroom folder of this directory.
A single test class holds a group of related test functions that test the correctness of my
models and API endpoints. For the third test the sersver must be running!! Below is a 
demonstration on each test class.
*******************************************************************************************
1.) Test class 1: python3 ./manage.py test chatroom.tests.MessageTestCase
2.) Test class 2: python3 ./manage.py test chatroom.tests.ChatTestCase 
3.) Test class 3: python3 ./manage.py runserver 
                  python3 ./manage.py test chatroom.tests.MessageAPITestCase

Note: Notice that on the 3rd test the server must be running!
