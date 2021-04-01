from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import createThreadForm


def basicResponse (request):
    return HttpResponse("Success")

