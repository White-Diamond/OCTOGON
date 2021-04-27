from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Message
import json

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def retrieve_conversation(request):
    # save messages in request.body
    data = json.loads(request.body)
    activeUser = data['to']
    otherUser = data['from']

    # Message exists
    chat1 = Message.objects.filter(to_id=activeUser, from_id=otherUser)
    chat2 = Message.objects.filter(to_id=otherUser, from_id=activeUser)

    if(chat1.exists() or chat2.exists()):
        # get conversation
        conversation = chat1.union(chat2).order_by('created_at').values('message', 'to_id', 'from_id')
        # convert from QuerySet to JSON string
        jsonMessages = json.dumps(list(conversation))
        # since messages have now been seen update seen to true=1
        chat1.update(seen=1)
        chat2.update(seen=1)

        return HttpResponse(jsonMessages)

    jsonMessages = json.dumps([])
    return HttpResponse(jsonMessages)

def retrieve_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    recipient_id = data['to']
    sender_id = data['from']

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

def load_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    message = data['message']
    recipient_id = data['to']
    sender_id = data['from']

    print(message)
    print(recipient_id)
    print(sender_id)

    # add message to Message model
    newMessage = Message()
    newMessage.to_id = recipient_id
    newMessage.from_id = sender_id
    newMessage.message = message
    newMessage.save()

    return HttpResponse("OK")
