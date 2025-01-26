from django.test import TestCase
from .models import *
from .requests import *
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

class UserRegistrationAPITest(APITestCase):
    def setUp(self):
        self.register_user_url = reverse('register_user')

    def test_successful_user_registration(self):
        response = self.client.post(self.register_user_url, {
            'username': 'test_user',
            'email': 'test@yaghoo.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'test_password',
            'role':'USER',
            'image':''
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
        
        
    
    
    
    
class CheckBookingAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and two profiles: one for a receptionist and another for a non-receptionist
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.receptionist_profile = Profile.objects.create(
            user=self.user,
            role='RECEPTIONIST'
        )
        self.non_receptionist_profile = Profile.objects.create(
            user=self.user,
            role='USER'
        )

        # Create a room
        self.room = Room.objects.create(
            image='path/to/image.jpg',  # Assuming 'image' can be nullable or provide a default image path
            floor=1,  # Provide a valid floor number
            type='STANDARD',  # Assuming you have a type field that requires a valid type
            available=True  # Set the availability status
        )
        # Create a booking
        self.booking = Booking.objects.create(
            room=self.room,
            start_date='2023-01-01',
            end_date='2023-01-05',
            user=self.user,
            status='PENDING'
        )

        # Authenticate as the user

    def test_approve_booking_by_receptionist(self):
        url = reverse('check_booking', args=[self.booking.id, self.receptionist_profile.id])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'APPROVED')

    def test_approve_booking_by_non_receptionist(self):
        url = reverse('check_booking', args=[self.booking.id, self.non_receptionist_profile.id])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_reject_booking_by_receptionist(self):
        url = reverse('check_booking', args=[self.booking.id, self.receptionist_profile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'REJECTED')

    def test_reject_booking_by_non_receptionist(self):
        url = reverse('check_booking', args=[self.booking.id, self.non_receptionist_profile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)