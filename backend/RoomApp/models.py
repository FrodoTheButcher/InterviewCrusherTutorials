from django.db import models

# Create your models here.
class Room(models.Model):
    def __init__(self, room_id, floor, room_type, available):
        self.room_id = room_id
        self.floor = floor
        self.room_type = room_type
        self.available = available
    room_id = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    floor = models.IntegerField()
    type = models.IntegerField() 
    available = models.BooleanField(default=False)

class Booking(models.Model):
    def __init__(self, user, room, start_date, end_date):
        self.user = user
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
    room = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()