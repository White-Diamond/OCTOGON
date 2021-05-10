from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Course
from accounts.decorators import unauthenticated_user


# Display Profile
@unauthenticated_user
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


# When the update button is pressed
@unauthenticated_user
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.username = request.POST.get('uname')
        user.email = request.POST.get('email')
        user.save()
    return redirect('/profilepage/')