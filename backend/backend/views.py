from .models import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def register_user_and_make_booking(self):
    email = input("Enter email: ")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    password = input("Enter password: ")
    
    user = User(email, first, last, password)
    
    rooms = [
        Room(101, 1, "Single", True),
        Room(102, 1, "Double", True),
        Room(103, 1, "Suite", False),
        Room(104, 2, "Single", True),
        Room(105, 2, "Double", False),
        Room(201, 2, "Suite", True),
        Room(202, 3, "Single", True),
        Room(203, 3, "Double", True),
        Room(204, 3, "Suite", True),
        Room(205, 4, "Single", False)
    ]
    
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
    print(f"Booking successful for {booking.user.email} from {booking.start_date} to {booking.end_date} in room {booking.room.room_id}")
