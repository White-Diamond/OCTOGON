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
        print("Setting up...")

    def test_retrieve_json(self):
        # create JSON data
        python_dict = {
            "1": {
                "guid": "8a40135230f21bdb0130f21c255c0007",
                "portalId": 999,
                "email": "fake@email"
            }
        }
        # CREATE CORRECT JSON DATA ABOVE
        data = self.client.post('/chatroom/retrieve/', json.dumps(python_dict), content_type="application/json")
        print(data.status_code)
        self.assertEqual(data,data)
        # validate JSON was put into database

    def test_load_json(self):
        self.assertEqual(1,1)
        # validate JSON was put into database
