from django.db import models
from django.contrib.auth.models import User
from RoomApp.models import Room

class Profile(models.Model):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('HOUSEKEEPER', 'Housekeeper'),
        ('MANAGER', 'Manager'),
        ('RECEPTIONIST', 'Receptionist'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    image = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='USER')

class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)