from .models import *
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from RoomApp.models import *
from .requests import CreateUserRequest , CreateRoomRequest
from drf_yasg.utils import swagger_auto_schema
class RegisterRoomView(APIView):
    @swagger_auto_schema(request_body=CreateRoomRequest)
    def post(self,request):
        try:
            floor = input("enter floor")
            type = input("enter type")
            Room.objects.create(floor = floor,type=type,available=True)
            return Response(data="success")
        except Exception as e:
            return Response(data="fail")
    
class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        return Response({"data": "Success", "user_id": user.id})
 
@api_view(['GET'])
def register_user_and_make_booking(self):
    email = input("enter user email")
    user = User.objects.get(email=email)
    rooms = Room.objects.all()
    
    print("Available Rooms:")
    for room in rooms:
        if room.available:
            print(f"Room ID {room.id}, Floor {room.floor}, Type {room.room_type}")
    
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
    
    booking = Booking(user, selected_room.id, start, end)
    Booking.objects.create(room = selected_room.id, start_date = start,end_Date = end,user = 1)
    print(f"Booking successful for {booking.user.email} from {booking.start_date} to {booking.end_date} in room {room_id}")
    return Response(data="success")