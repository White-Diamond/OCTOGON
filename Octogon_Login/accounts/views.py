from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout   # login info

from django.contrib import messages # success message

from .forms import CreateUserForm

def signup(request):
  form = CreateUserForm()
  context = {'register': form}

  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account was created for ' + user)
      return redirect('login')
    else:
      messages.info(request, 'Account was not created')

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
      return redirect("base")
    else:
      messages.info(request, "Username or Password is incorrect")
  return render(request, 'registration/login.html', context)

def LoginSignUpFunction(request):
  if request.method == "POST":
    signin_button = request.POST.get('button-name', False)

    if signin_button == 'login_check':
      ##Carry out appropriate login function
      loginPage(request=request)

    else:
      ##Carry out appropriate register function
      signup(request=request)

  form_register = CreateUserForm()
  context={
      "register":form_register
    }

  return render(request, "registration/login.html", context)


# def logoutUser(request):
#   context = {}
#   return render(request, '', context)


def base(request):
  return render(request, 'base.html')

def pswrd(request):
  return render(request, 'registration/password_reset_form.html')
