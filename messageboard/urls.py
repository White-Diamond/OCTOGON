from django.urls import path

from messageboard.views import basicResponse
from messageboard.views import mainBoard
from messageboard.views import getThreadPosts
from messageboard.views import userMakesThread
from post.models import Thread

urlpatterns = [
    path('basicRes/', basicResponse),
    path('messageboard/', mainBoard),
    path('thread/<int:thrdID>/', getThreadPosts),
    path('threadcreate/', userMakesThread),
]