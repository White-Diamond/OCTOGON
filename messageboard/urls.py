from django.urls import path

from messageboard.views import basicResponse
from messageboard.views import mainBoard
from messageboard.views import threadBoard
from messageboard.views import getThreadPosts

urlpatterns = [
    path('basicRes/', basicResponse),
    path('messageboard/', mainBoard),
    path('threadpage/', threadBoard),
    path('thread/', getThreadPosts)
]