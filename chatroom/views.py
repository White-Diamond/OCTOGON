from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Chat, Message
import json

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def retrieve_json(request):
    # save messages in request.body
    data = json.loads(request.body)
    recipient_id = data['recipient']['username']
    sender_id = data['sender']['username']

    # find chatroom ID in Chat model
    chatID = Chat.objects.get(to_id=sender_id, from_id=recipient_id)

    # get all messages with chat id
    chatMessages = Message.objects.filter(chat=chatID)

    # get an ordered QuerySet of all unseen messages
    orderedMessagesByDate = chatMessages.filter(seen=0).order_by('created_at').values('message')

    # convert to QuerySet to JSON string
    jsonMessages = json.dumps(list(orderedMessagesByDate))

    # since messages have no been see update seen to 
    orderedMessagesByDate.update(seen=1)

    return HttpResponse(jsonMessages)

def load_json(request):
    # save messages in request.body
    data = json.loads(request.body)
    message = data['message']
    recipient_id = data['recipient']['username']
    sender_id = data['sender']['username']

    # find chatroom ID in Chat model
    chat = Chat.objects.get(to_id=recipient_id, from_id=sender_id)

    # add message to Message model
    newMessage = Message()
    newMessage.message = message
    newMessage.chat = chat
    newMessage.save()

    return HttpResponse("OK")
