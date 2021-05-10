# Project Octogon

*******************************************************************************************
TEST INSTRUCTIONS (Django native test suite):
*******************************************************************************************


*******************************************************************************************
CHATROOM MODULE TESTS
*******************************************************************************************
There are 3 test classes. Each class is in test.py in the chatroom folder of this directory.
A single test class holds a group of related test functions that test the correctness of my
models and API endpoints. For the 2nd test the server must be running!! Additionally, there
are tests for the front-end that ues the selenium library. To run these tests go to the 
selenium folder in the chatroom directory and run the test.py file. Below is a demonstration 
on how to run each test case.

1.) Test all classes        :   python3 ./manage.py test chatroom.tests
2.) Test the API test case  :   python3 ./manage.py runserver 
                                python3 ./manage.py test chatroom.tests.MessageAPITestCase
3.) Selenium tests          :   python3 test.py

Note: Notice that on the 2nd test the server must be running!
      For the 3rd test you must uncomment the decorator in views.py
*******************************************************************************************


*******************************************************************************************
PROFILEPAGE MODULE TESTS
*******************************************************************************************
Ryan’s front-end selenium tests work, but only if a user with the username "test" is 
already stored in the database. For this reason, he commented out the front-end section 
of his tests. Automated testing on the profilepage app is not feasible at the moment 
because we have no system of storing users in the database and tracking a current user. In 
its current state, the app relies on a user with the username “test” being present in the 
database when the runserver command is used. He used this approach to move forward on this 
issue while we hash out how to track current users. It should only take one line of code 
in views to add the desired functionality. He was able to confirm the frontend tests work 
by manually entering a “test” user through the admin page. The backend tests still work 
by following the instructions above.
*******************************************************************************************
