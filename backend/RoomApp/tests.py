from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from RoomApp.models import Room , Booking
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

class UserRegistrationAPITest(APITestCase):
    def setUp(self):
        self.register_user_url = reverse('register_user')

    def test_successful_user_registration(self):
        response = self.client.post(self.register_user_url, {
            'username': 'test_user',
            'email': 'test@yaghoo.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'test_password'
        }, format='json')  # Same here, format='json'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.email, 'test@yaghoo.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')



class RegisterBookingViewTest(APITestCase):
    def setUp(self):
        self.booking_url = reverse('register_booking')
        # Create a user
        self.user = User.objects.create(
            username='testuser', email='test@user.com', password='testpassword'
        )
        # Create a room
        self.room = Room.objects.create(floor=1, type='suite', available=True)
    
    def test_successful_booking(self):
        response = self.client.post(self.booking_url, {
            'email': 'test@user.com',
            'room_id': self.room.id,
            'start_date': '2025-01-01',
            'end_date': '2025-01-02'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(Room.objects.get(id=self.room.id).available)  # Room should now be unavailable
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_unavailable_room(self):
        self.room.available = False
        self.room.save()
        response = self.client.post(self.booking_url, {
            'email': 'test@user.com',
            'room_id': self.room.id,
            'start_date': '2025-01-01',
            'end_date': '2025-01-02'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_booking_nonexistent_room(self):
        response = self.client.post(self.booking_url, {
            'email': 'test@user.com',
            'room_id': 999,  # Non-existent room ID
            'start_date': '2025-01-01',
            'end_date': '2025-01-02'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        Booking.objects.all().delete()
        Room.objects.all().delete()
        User.objects.all().delete()