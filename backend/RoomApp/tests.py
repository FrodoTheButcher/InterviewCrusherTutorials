from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from RoomApp.models import Room 
from django.contrib.auth.models import User

class RoomRegistrationAPITest(APITestCase):
    def setUp(self):
        self.register_room_url = reverse('register_room')

    def test_successful_room_registration(self):
        response = self.client.post(self.register_room_url, {
            'floor': 1, 
            'type': 'suite'
        }, format='json')  # format='json' handles content_type automatically
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify that room was indeed added
        self.assertEqual(Room.objects.count(), 1)
        room = Room.objects.first()
        self.assertEqual(room.floor, 1)
        self.assertEqual(room.type, 'suite')
        self.assertTrue(room.available)
