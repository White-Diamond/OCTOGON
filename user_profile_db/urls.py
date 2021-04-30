from django.urls import path

from . import views

app_name = 'user_profile_db'
urlpatterns = [
    path('addclass/', views.add_class),
    path('removeclass/', views.remove_class),
    #path('',),
]