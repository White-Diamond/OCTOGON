from django.test import TestCase
from .models import Message
import json

class MessageTestCase(TestCase):
    def setUp(self):
        # setup all necessary models for tests
        Message.objects.create(to_id="joshua.caleb.bender@gmail.com", from_id="jbender321@gmail.com", message="Hi!", seen=0)
    
    def test_message(self):
        # get message out
        query = Message.objects.get(message="Hi!")
        # assert equality
        self.assertEqual(query.message, "Hi!")

    def test_seen(self):
        # get seen boolean value out of db
        query = Message.objects.get(message="Hi!", seen=0)
        # assert equality
        self.assertEqual(query.seen, 0)

class MessageAPITestCase(TestCase):
    def setUp(self):
        # setup all necessary models for tests
        Message.objects.create(to_id="bill.bob@gmail.com", from_id="jacob.bender@gmail.com", message="Hi")

    def test_load_json(self):
        # create JSON data
        python_dict = {
            "message": "json",
            "from": "jacob.bender@gmail.com",
            "to": "ben.bender@gmail.com"
        }

        # POST
        data = self.client.post('/chatroom/load_message/', json.dumps(python_dict), content_type="application/json")

        # validate JSON response was OK
        successHTTP = 200
        self.assertEqual(data.status_code, successHTTP)

        # validate message JSON was sent to db
        message = Message.objects.get(message="json")
        self.assertEqual(message.message, "json")