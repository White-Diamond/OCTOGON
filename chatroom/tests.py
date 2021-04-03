from django.test import TestCase
from .models import Chat, Message
import json

# Create your tests here.
class ChatTestCase(TestCase):
    def setUp(self):
        # setup all necessary models for tests
        Chat.objects.create(to_id="joshua.caleb.bender@gmail.com", from_id="jbender321@gmail.com")
    
    def test_to_id(self):
        # get to_id out
        chat = Chat.objects.get(to_id="joshua.caleb.bender@gmail.com")
        # assert equality
        self.assertEqual(chat.to_id, "joshua.caleb.bender@gmail.com")
        
    def test_from_id(self):
        # get to_id out
        chat = Chat.objects.get(from_id="jbender321@gmail.com")
        # assert equality
        self.assertEqual(chat.from_id, "jbender321@gmail.com")


class MessageTestCase(TestCase):
    def setUp(self):
        # setup all necessary models for tests
        Chat.objects.create(to_id="joshua.caleb.bender@gmail.com", from_id="jbender321@gmail.com")
        chat = Chat.objects.get(to_id="joshua.caleb.bender@gmail.com")
        Message.objects.create(chat=chat, message="Hi!", seen=0)
    
    def test_message(self):
        # get message out
        message = Message.objects.get(message="Hi!")
        # assert equality
        self.assertEqual(message.message, "Hi!")

    def test_seen(self):
        # get seen boolean value out of db
        seen = Message.objects.get(message="Hi!", seen=0)
        # assert equality
        self.assertEqual(seen.seen, 0)

class MessageAPITestCase(TestCase):
    def setUp(self):
        # setup all necessary models for tests
        Chat.objects.create(to_id="joshua.caleb.bender@gmail.com", from_id="jbender321@gmail.com")
        Chat.objects.create(to_id="jbender321@gmail.com", from_id="joshua.caleb.bender@gmail.com")

    def test_retrieve_json(self):
        # create JSON data
        python_dict = {
            "sender": {
                "fullName": "Josh Bender", 
                "username": "joshua.caleb.bender@gmail.com"
            }, 
            "recipient": {
                "fullName": "Jacob Bender", 
                "username": "jbender321@gmail.com"
            }
        }

        # POST
        data = self.client.post('/chatroom/retrieve/', json.dumps(python_dict), content_type="application/json")

        # validate JSON response was OK
        successHTTP = 200
        self.assertEqual(data.status_code, successHTTP)

    def test_load_json(self):
        # create JSON data
        python_dict = {
                "message": "json",
                "recipient": {
                    "fullName": "Jacob Bender",
                    "username": "jbender321@gmail.com"
                },
                "sender": {
                    "fullName": "Josh Bender",
                    "username": "joshua.caleb.bender@gmail.com"
                }
        }

        # POST
        data = self.client.post('/chatroom/load/', json.dumps(python_dict), content_type="application/json")

        # validate JSON response was OK
        successHTTP = 200
        self.assertEqual(data.status_code, successHTTP)

        # validate message JSON was sent to db
        message = Message.objects.get(message="json")
        self.assertEqual(message.message, "json")


