from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Course


def index(request):
    data = User.objects.get(username="test")
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

