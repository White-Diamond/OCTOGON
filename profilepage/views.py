from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Course

def index(request):

    data = Profile.objects.get(user=request.user)

    #show yes or no insteasd of true and false
    if (data.is_instructor):
        ins = 'Yes'
    else:
        ins = 'No'
    context = {
        'firstname': data.user.first_name,
        'lastname': data.user.last_name,
        'username': data.user.username,
        'email': data.user.email,
        'instructor': ins,
        'courses': data.courses,
    }
    return render(request, "profilepage.html", context)
