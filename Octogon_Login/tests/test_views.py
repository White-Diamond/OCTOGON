from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.base = reverse("base")
    self.pswrd = reverse("pswrd")

  def test_base_GET(self):
    response = self.client.get(self.base)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, "base.html")

  def test_pswrd_GET(self):
    response = self.client.get(self.pswrd)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, "registration/password_reset_form.html")
