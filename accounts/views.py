from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login  # login info
from django.contrib.auth.decorators import login_required # login must be required to access view.
                                                          #template: @login_required(login_url="") (place above a function)
from django.contrib.auth.models import Group
from django.contrib import messages # success message
from datetime import datetime # date display for homepage

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users # checks user authentication

def error_404_view(request, exception):
  return render(request, '404.html') 

def signup(request):
  form = CreateUserForm()
  context = {'register': form}

  if request.method == "POST":
    form = CreateUserForm(request.POST)

    if form.is_valid():
      user = form.save()

      username = form.cleaned_data.get('username')

      group = Group.objects.get(name='student')
      user.groups.add(group)
      
      messages.success(request, 'Account was created for ' + username)
      return redirect('login')
    else:
      messages.info(request, 'Account was not created')
      messages.error(request, form.errors)

  return render(request, 'registration/login.html', context)

def loginPage(request):
  context = {}

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    # valid user
    if user is not None:
      login(request, user)
      return redirect("messageboard") # url may change over time
    else:
      messages.info(request, "Username or Password is incorrect")
  return render(request, 'registration/login.html', context)

@unauthenticated_user
def LoginSignUpFunction(request):
  if request.method == "POST":
    signin_button = request.POST.get('button-name', False)

    if signin_button == 'login_check':
      ##Carry out appropriate login function
      context = {}

      if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # valid user
        if user is not None:
          login(request, user)
          return redirect("/messageboard") # url may change over time
        else:
          messages.info(request, "Username or Password is incorrect")
    else:
      ##Carry out appropriate register function
      signup(request=request)

  form_register = CreateUserForm()
  context={
      "register":form_register
    }

  return render(request, "registration/login.html", context)

def base(request):
  return render(request, 'base.html')

def pswrd(request):
  return render(request, 'registration/password_reset_form.html')
