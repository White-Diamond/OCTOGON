from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Course


def index(request):
    #This app will not work unless a user with the username "test" is already stored in the database
    #I used this approach to move forward on this story while we hash out how to track current users
    #The following line will change later when we have a system of storing current user
    data = UserProfile.objects.get(username="test")
    #all other code is working as intended when testing with admin page

    #show yes or no insteasd of true and false
    if (data.is_instructor):
        ins = 'Yes'
    else:
        ins = 'No'
    context = {
        'firstname': data.name_first,
        'lastname': data.name_last,
        'username': data.username,
        'email': data.email,
        'instructor': ins,
        'courses': data.courses,
    }
    return render(request, "profilepage.html", context)

