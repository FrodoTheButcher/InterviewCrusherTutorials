from django.db import models
from django.contrib.auth.models import User
from RoomApp.models import Room
class Profile(models.Model):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('HOUSEKEEPER', 'Housekeeper'),
        ('MANAGER', 'Manager'),
        ('RECEPTIONIST', 'Receptionist'),
        ('DEVELOPER','Developer'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='USER')

class UserRegistrationRequest(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    role = models.CharField(choices = Profile.ROLE_CHOICES, max_length=100)
    
class Booking(models.Model):
    CHOICES = [
        ('PENDING','Pending'),
        ('APPROVED','Approved'),
        ('REJECTED','Rejected')
    ]
    room = models.ForeignKey(Room,on_delete=models.CASCADE,default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cost = models.FloatField(null=False,blank=False,default=0.0)
    status = models.CharField(max_length=10, choices=CHOICES, default='PENDING')
