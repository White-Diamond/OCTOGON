from django.urls import path
from accounts import views

urlpatterns = [
  path('login/', views.LoginSignUpFunction, name="login"),
  path('base/', views.base, name='base'),
  path('password_reset_form/', views.pswrd, name='pswrd'),
]
