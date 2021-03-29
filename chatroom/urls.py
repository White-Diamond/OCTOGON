from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_page),
    path('retrieve/', views.retrieve_json),
    path('load/', views.load_json),
]
