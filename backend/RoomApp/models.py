from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('STANDARD', 'Standard'),
        ('DELUXE', 'Deluxe'),
        ('SUITE', 'Suite'),
        ('FAMILY', 'Family Room'),
    ]
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    floor = models.IntegerField()
    type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES) 
    available = models.BooleanField(default=False)

