from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Chat, Message
import json

# Create your views here.
def chat_page(request):
    return render(request, "index.html")

def create_new_chat(request):
    # request data
    data = json.loads(request.body)
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # already exists
    chatExists = Chat.objects.filter(to_id=recipient_id, from_id=sender_id).exists()

    # new chat
    if(chatExists == False):
        newChat = Chat()
        newChat.to_id = recipient_id
        newChat.from_id = sender_id
        newChat.save()

    return HttpResponse("OK") 

def retrieve_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # doesn't exist
    chatExists = Chat.objects.filter(to_id=recipient_id, from_id=sender_id).exists()

    if(chatExists == True):
        # find chatroom ID in Chat model
        chatID = Chat.objects.get(to_id=recipient_id, from_id=sender_id)

        # get chat messages
        chatMessages = Message.objects.filter(chat=chatID)

        # get an ordered QuerySet of all unseen messages
        orderedMessagesByDate = chatMessages.filter(seen=0).order_by('created_at').values('message')

        # convert from QuerySet to JSON string
        jsonMessages = json.dumps(list(orderedMessagesByDate))

        # since messages have now been see update seen to true=1
        orderedMessagesByDate.update(seen=1)

        return HttpResponse(jsonMessages)
    

    jsonMessages = json.dumps({})
    return HttpResponse(jsonMessages)


def load_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    message = data['message']
    recipient_id = data['to']['email']
    sender_id = data['from']['email']

    # find chatroom ID in Chat model
    chat = Chat.objects.get(to_id=recipient_id, from_id=sender_id)

    # add message to Message model
    newMessage = Message()
    newMessage.message = message
    newMessage.chat = chat
    newMessage.save()

    return HttpResponse("OK")
