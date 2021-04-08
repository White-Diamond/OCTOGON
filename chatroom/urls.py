from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page),
    path('create/', views.create_new_chat),
    path('retrieve/', views.retrieve_message),
    path('load/', views.load_message)
]
