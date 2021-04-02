from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def retrieve_json(request):
    return JsonResponse({'foo':'retrieve_json'})

def load_json(request):
    # save messages in request.body
    print(request.body)
    return HttpResponse("OK")
