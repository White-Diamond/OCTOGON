from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import base, pswrd, SignUpView

# names: signup

class TestUrls(SimpleTestCase):

  def test_signup_url_resolves(self):
    url = reverse("signup")
    self.assertEquals(resolve(url).func.view_class, SignUpView)

  def test_base_url_resolves(self):
    url = reverse("base")
    self.assertEquals(resolve(url).func, base)

  def test_pswrd_url_resolves(self):
    url = reverse("pswrd")
    self.assertEquals(resolve(url).func, pswrd)
