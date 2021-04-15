from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Message
import json

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def retrieve_conversation(request):
    return HttpResponse("OK")

def retrieve_active_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # Message exists
    chat = Message.objects.filter(to_id=recipient_id, from_id=sender_id)

    if(chat.exists()):
        # get an ordered QuerySet of all unseen messages
        orderedMessagesByDate = chat.filter(seen=0).order_by('created_at').values('message')

        # convert from QuerySet to JSON string
        jsonMessages = json.dumps(list(orderedMessagesByDate))

        # since messages have now been seen update seen to true=1
        orderedMessagesByDate.update(seen=1)

        return HttpResponse(jsonMessages)

    jsonMessages = json.dumps({})
    return HttpResponse(jsonMessages)

def retrieve_inactive_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # Message exists
    chat = Message.objects.filter(to_id=recipient_id, from_id=sender_id).values('message', 'from_id')
    print(chat)

    if(chat.exists()):
        # convert from QuerySet to JSON string
        jsonMessages = json.dumps(list(chat))
        print(jsonMessages)

        # since messages have now been seen update seen to true=1
        chat.update(seen=1)

        return HttpResponse(jsonMessages)

    jsonMessages = json.dumps([])
    return HttpResponse(jsonMessages)

def load_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    message = data['message']
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # add message to Message model
    newMessage = Message()
    newMessage.to_id = recipient_id
    newMessage.from_id = sender_id
    newMessage.message = message
    newMessage.save()

    return HttpResponse("OK")
