from django.db import models

# Create your models here.
class Room(models.Model):
    image = models.TextField(blank=True, null=True)
    floor = models.IntegerField()
    type = models.CharField(max_length=50) 
    available = models.BooleanField(default=False)

class Booking(models.Model):
    room = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()