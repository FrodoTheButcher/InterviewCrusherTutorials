from django.db import models

class User():
    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=150)

class Room():
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

class Booking():
    def __init__(self, user, room, start_date, end_date):
        self.user = user
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
    room = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()