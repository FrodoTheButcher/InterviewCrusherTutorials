from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from RoomApp.models import Room
from django.contrib.auth.models import User
class RegisterRoomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_room_url = reverse('register_room') 
        self.register_user_url = reverse('register_user')
    def test_successful_room_registration(self):
        response = self.client.post(self.register_room_url, {
            'floor': 1, 
            'type': 'suite'
        }, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify that room was indeed added
        self.assertEqual(Room.objects.count(), 1)
        room = Room.objects.first()
        self.assertEqual(room.floor, 1)
        self.assertEqual(room.type, 'suite')
        self.assertTrue(room.available)
    def test_successful_user_registration(self):
        response = self.client.post(self.register_user_url,{
            'email':"test@yaghoo.com",
            'first_name':'test_first_mna,e',
            'last_name':'test_l;ast_name',
            'password':'test_password'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def tearDown(self):
        Room.objects.all().delete()
        User.objects.all().delete()