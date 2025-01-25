from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    image = models.TextField(blank=True, null=True)
    floor = models.IntegerField()
    type = models.CharField(max_length=50) 
    available = models.BooleanField(default=False)

class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)