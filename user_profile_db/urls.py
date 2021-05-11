from django.urls import path

from . import views

app_name = 'user_profile_db'
urlpatterns = [
    path('addcourse/', views.add_course),
    path('removecourse/', views.remove_course),
    path('managecourses/', views.course_selection, name="coursechange-page"),
]