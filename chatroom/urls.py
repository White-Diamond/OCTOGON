from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page),
    path('load_message/', views.load_message),
    path('retrieve_active_message/', views.retrieve_active_message),
    path('retrieve_inactive_message/', views.retrieve_inactive_message),
    path('retrieve_conversation/', views.retrieve_conversation)
]
