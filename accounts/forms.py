from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from profilepage.models import UserProfile

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
  class Meta:
    model = UserProfile
    fields = ['name_first', 'name_last', 'is_instructor', 'courses']
