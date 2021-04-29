from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Course

def index(request):

    data = Profile.objects.get(duser=request.user)

    #show yes or no insteasd of true and false
    if (data.is_instructor):
        ins = 'Yes'
    else:
        ins = 'No'
    context = {
        'firstname': data.name_first,
        'lastname': data.name_last,
        'username': data.duser.username,
        'email': data.duser.email,
        'instructor': ins,
        'courses': data.courses,
    }
    return render(request, "profilepage.html", context)
