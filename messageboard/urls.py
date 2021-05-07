from django.urls import path

from messageboard.views import basicResponse
from messageboard.views import mainBoard
from messageboard.views import getThreadPosts
from messageboard.views import userMakesThread
from messageboard.views import userMakesPost

urlpatterns = [
     path('messageboard/', mainBoard, name="main-messageboard"),
     path('basicRes/', basicResponse),
     path('messageboard/thread/<int:thrdID>/', getThreadPosts),
     path('threadcreate/', userMakesThread),
     path('newpost/<int:thrdID>', userMakesPost),
 ]