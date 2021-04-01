from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from messageboard.models import tempThreadModel
from .forms import createThreadForm


def basicResponse (request):
    return HttpResponse("Success")

# View of the main messageboard
def mainBoard (request):
    threads = {}
    threads['threadList'] = tempThreadModel.objects.all()
    return render(request, "board.html", threads)

# View specific to a certain thread
def threadBoard(request):
    return HttpResponse("Thread specific webpage placeholder")

def getThreadPosts (request):
    posts = {}
    posts = models.tempPosts.objects.all()
    return JsonResponse(posts)