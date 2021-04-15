# Project Octogon

*******************************************************************************************
TEST INSTRUCTIONS (Django native test suite):
*******************************************************************************************
I have 2 test classes. Each class is in test.py in the chatroom folder of this directory.
A single test class holds a group of related test functions that test the correctness of my
models and API endpoints. For the 2nd test the server must be running!! Below is a 
demonstration on each test class.
*******************************************************************************************
1.) Test class 1: python3 ./manage.py test chatroom.tests.MessageTestCase
3.) Test class 2: python3 ./manage.py runserver 
                  python3 ./manage.py test chatroom.tests.MessageAPITestCase

Note: Notice that on the 2nd test the server must be running!