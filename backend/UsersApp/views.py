
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .requests import CreateUserRequest , BookingRequest
from .models import Booking
from RoomApp.models import Room
class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self, request):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return Response({"message": "User registered successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)




class RegisterBookingView(APIView):
    @swagger_auto_schema(request_body=BookingRequest)
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)

        room_id = request.data.get('room_id')
        try:
            selected_room = Room.objects.get(id=room_id)
            if not selected_room.available:
                return Response("Room not available.", status=status.HTTP_400_BAD_REQUEST)
        except Room.DoesNotExist:
            return Response("Room does not exist.", status=status.HTTP_404_NOT_FOUND)

        start = request.data.get('start_date')
        end = request.data.get('end_date')

        booking = Booking.objects.create(
                room=selected_room,
                start_date=start,
                end_date=end,
                user=user,
            )
        selected_room.available = False
        selected_room.save()

        return Response({
            "message": "Booking successful",
            "details": {
                "user": user.email,
                "room_id": selected_room.id,
                "start_date": booking.start_date,
                "end_date": booking.end_date
            }
        }, status=status.HTTP_201_CREATED)