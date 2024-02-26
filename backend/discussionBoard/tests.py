from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Message
from django.contrib.auth.models import User
# Create your tests here.

class MessageTest(TestCase):
    def setUp(self):
        j = User.objects.create_user(first_name="john", email="lennon@thebeatles.com", password="johnpassword",username="JohnTheUser")
        Message.objects.create(user=j, message="This is a test message")
    
    def test_message_creation(self):
        mess1 = Message.objects.get(id=1)
        self.assertEqual(mess1.message, "This is a test message")
        self.assertEqual(mess1.user.email, "lennon@thebeatles.com")