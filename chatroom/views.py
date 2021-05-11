from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from .models import Message, UserList
from django.contrib.auth.models import User
from accounts.decorators import unauthenticated_user
import json

# Create your views here.
@unauthenticated_user
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
        conversation = chat1.union(chat2).order_by('created_at').values('message', 'to_id', 'from_id', 'seen', 'created_at')
        # convert from QuerySet to list
        conversationList = list(conversation)
        # convert to date time
        for message in conversationList:
            utc_time = message['created_at']
            message['created_at'] = utc_time.strftime("%m/%d/%Y, %H:%M")
        # convert to JSON string
        jsonMessages = json.dumps(list(conversationList))

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
        orderedMessagesByDate = chat.filter(seen=0).order_by('created_at').values('message', 'created_at')
        # convert from QuerySet to list
        messageList = list(orderedMessagesByDate)
        # convert to date time
        for message in messageList:
            utc_time = message['created_at']
            message['created_at'] = utc_time.strftime("%m/%d/%Y, %H:%M")
        # convert to JSON string
        jsonMessages = json.dumps(messageList)

        return HttpResponse(jsonMessages)

    jsonMessages = json.dumps([])
    return HttpResponse(jsonMessages)

def load_message(request):
    # save messages in request.body
    data = json.loads(request.body)
    message = data['message']
    recipient_id = data['to']
    sender_id = data['from']

    # add message to Message model
    newMessage = Message()
    newMessage.to_id = recipient_id
    newMessage.from_id = sender_id
    newMessage.message = message
    newMessage.seen = 0
    newMessage.save()

    return HttpResponse("OK")

def retrieve_user_list(request):
    # save messages in request.body
    data = json.loads(request.body)
    activeUser = data['activeUser']

    # Message exists
    userList = UserList.objects.filter(active_user=activeUser).values('other_user', 'has_notification')

    if(userList.exists()):
        # convert from QuerySet to JSON string
        jsonList = json.dumps(list(userList))
        return HttpResponse(jsonList)

    jsonList = json.dumps([])
    return HttpResponse(jsonList)

def load_user_list(request):
    # save user list in request.body
    data = json.loads(request.body)
    activeUser = data['activeUser']
    otherUsers = data['otherUsers']

    # add message to Message model
    UserList.objects.filter(active_user=activeUser).delete()
    for user in otherUsers:
        UserList.objects.create(active_user=activeUser, other_user=user['other_user'], has_notification=user['has_notification'])

    return HttpResponse("OK")

def update_messages_as_seen(request):
    # save messages in request.body
    data = json.loads(request.body)
    activeUser = data['to']
    otherUser = data['from']

    # Message exists
    chat1 = Message.objects.filter(to_id=activeUser, from_id=otherUser, seen=0)
    chat2 = Message.objects.filter(to_id=otherUser, from_id=activeUser, seen=0)

    if(chat1.exists() or chat2.exists()):
        # update all messages as seen
        chat1.update(seen=1)
        chat2.update(seen=1)

    return HttpResponse("OK")

def get_all_student_users(request):
    # username
    usernameList = User.objects.filter(groups__name='student').values('username')
    jsonList = json.dumps(list(usernameList))
    return HttpResponse(jsonList)