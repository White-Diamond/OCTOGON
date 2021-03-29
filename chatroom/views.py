from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def retrieve_json(request):
    return JsonResponse({'foo':'retrieve_json'})

def load_json(request):
    return JsonResponse({'foo':'load_json'})