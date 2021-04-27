from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page),
    path('load_message/', views.load_message),
    path('retrieve_message/', views.retrieve_message),
    path('retrieve_conversation/', views.retrieve_conversation)
]
