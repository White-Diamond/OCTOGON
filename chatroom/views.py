from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def chat_page(request):
    return JsonResponse({'foo': 'chat_page'})

def retreive_json(request):
    return JsonResponse({'foo':'retreive_json'})

def load_json(request):
    return JsonResponse({'foo':'load_json'})