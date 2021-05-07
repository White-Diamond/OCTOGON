from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page, name='chatroom-page'),
    path('load_message/', views.load_message),
    path('load_user_list/', views.load_user_list),
    path('retrieve_message/', views.retrieve_message),
    path('retrieve_conversation/', views.retrieve_conversation),
    path('retrieve_user_list/', views.retrieve_user_list)
]
