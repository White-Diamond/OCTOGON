# Login Tests Readme

## Version:<br>
  - This code was published in iteration 3<br>

## Dependencies:<br>
  - The testing functions currently utilizes django.test out the .py code
  - The testing functions can be found at “tests/.”
  - These testing scripts may change in the future once I utilize more Django code in my HTML files in future iterations
  - You will need to install: python, pip, and django to run these tests

## How to Run It?<br>
  - Follow these instructions to run the server tests for the first time:
    - Make sure you are located in the OCTOGON/Octogon_Login/ directory
    - follow [these](https://pip.pypa.io/en/stable/installing/) instructions if you don't have pip installed
    - pip install django
    - python manage.py migrate
    - python manage.py test

  - Follow these instructions once you have already installed everything above:
    - python manage.py test

  - The results of the tests will be displayed in the terminal
