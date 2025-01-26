
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .requests import CreateUserRequest , BookingRequest
from .models import Booking, Profile
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
    DAILY_RATES = {
        'STANDARD': 100,
        'DELUXE': 150,
        'SUITE': 200,
        'FAMILY': 180,
    }
    def get_cost(self, total_days, room_type):
        rate = self.DAILY_RATES.get(room_type, 0)
        return total_days * rate
        
    
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
        
        total_days = (end - start).days
        if total_days < 1:
            return Response("Invalid dates.", status=status.HTTP_400_BAD_REQUEST)
        
        booking = Booking.objects.create(
                room=selected_room,
                start_date=start,
                end_date=end,
                user=user,
                status = "PENDING"
            )

        return Response({
            "message": "Booking successful",
            "details": {
                "user": user.email,
                "room_id": selected_room.id,
                "start_date": booking.start_date,
                "end_date": booking.end_date
            }
        }, status=status.HTTP_201_CREATED)
        
        
class CheckBooking(APIView):
    def put(self,request,booking_id,profile_id):
        profile = Profile.objects.get(id=profile_id)
        if profile.role != "RECEPTIONIST":
            return Response({"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
        
        booking = Booking.objects.get(id=booking_id)
        booking.status = "APPROVED"
        room = booking.room
        room.available = False
        room.save()
        #save some approved bookings
        return Response({
            "message":"Booking saved",
        },status=status.HTTP_200_OK)
        
    def delete(self,request,booking_id,profile_id):
        profile = Profile.objects.get(id=profile_id)
        if profile.role != "RECEPTIONIST":
            return Response({"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
        #send email to the user
        booking = Booking.objects.get(id=booking_id)
        booking.status = "REJECTED"
        booking.save()
        return Response({
            "message":"Booking deleted",
        },status=status.HTTP_200_OK)
    