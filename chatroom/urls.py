from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page),
    path('retreive/', views.retreive_json),
    path('load/', views.load_json),
]
