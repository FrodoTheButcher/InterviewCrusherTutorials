from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from RoomApp.models import *
@api_view(['POST'])
def register_room(self):
    try:
        floor = input("enter floor")
        type = input("enter type")
        Room.objects.create(floor = floor,type=type,available=True)
        return Response(data="success")
    except Exception as e:
        return Response(data="fail")
 
@api_view(['GET'])
def register_user_and_make_booking(self):
    email = input("Enter email: ")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    password = input("Enter password: ")
    
    user = User(email, first, last, password)
    user.email = email 
    user.first_name = first 
    user.last_name = last 
    user.password = password
    
    rooms = Room.objects.all()
    
    print("Available Rooms:")
    for room in rooms:
        if room.available:
            print(f"Room ID {room.room_id}, Floor {room.floor}, Type {room.room_type}")
    
    room_id = int(input("Choose a room by Room ID: "))
    selected_room = None
    for room in rooms:
        if room.room_id == room_id and room.available:
            selected_room = room
            break       
    if not selected_room:
        print("Invalid room selection or room not available.")
        return
    
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    
    booking = Booking(user, selected_room.room_id, start, end)
    print(f"Booking successful for {booking.user.email} from {booking.start_date} to {booking.end_date} in room {room_id}")
    return Response(data="success")