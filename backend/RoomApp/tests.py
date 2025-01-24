from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from RoomApp.models import Room

class RegisterRoomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register_room') 

    def test_successful_room_registration(self):
        response = self.client.post(self.url, {
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

    def tearDown(self):
        Room.objects.all().delete()
