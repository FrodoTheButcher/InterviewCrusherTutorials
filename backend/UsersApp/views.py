
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import APIView , api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .requests import CreateUserRequest , BookingRequest
from .models import Booking, Profile , UserRegistrationRequest
from RoomApp.models import Room
from datetime import datetime
from .serializers import BookingSerializer , UserSerializer  , UserRegistrationRequestSerializer
from django.core.mail import send_mail
from django.conf import settings

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self, request):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        username = request.data.get("username")

        user = UserRegistrationRequest(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.save()
        send_mail("Account registration in pending","Your account will be validated by the admin soon",settings.EMAIL_HOST_USER,[request.data.get('email')],fail_silently=False)
        return Response({"message": "User registered successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)

    def get(self,request):
        users = UserRegistrationRequest.objects.all()
        users_serialized = UserRegistrationRequestSerializer(users,many=True).data 
        return Response(users_serialized,status=status.HTTP_200_OK)
    
    
class UpdateRegistrationRequest(APIView):
    def delete(self,request,pk):
        UserRegistrationRequest.objects.delete(id=pk)
        send_mail("Your registration was declined","Your registration was declined. You can contact us on ... for details",settings.EMAIL_HOST_USER,[request.data.get('email')],fail_silently=False)
        return Response(status=status.HTTP_200_OK)
    def post(self,request,pk):
        user_registration = UserRegistrationRequest.objects.get(id=pk)
        create_user  = User(
            email=user_registration.email,
            first_name=user_registration.first_name,
            last_name=user_registration.last_name,
            username=user_registration.username,
        )
        create_user.set_password(user_registration.password)
        send_mail("Your registration was accepted","Your registration was accepted. Login at ...",settings.EMAIL_HOST_USER,[request.data.get('email')],fail_silently=False)
        return Response(status=status.HTTP_200_OK)
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

          # Parse the start and end dates from the request data
        start = request.data.get('start_date')
        end = request.data.get('end_date')
        
        # Convert the start and end date strings to date objects
        start_date = datetime.strptime(start, '%Y-%m-%d').date() if start else None
        end_date = datetime.strptime(end, '%Y-%m-%d').date() if end else None       
        
        total_days = (end_date - start_date).days
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
        booking.save()
        room = booking.room
        room.available = False
        room.save()
       
        send_mail("Booking approved","Your booking was approved",settings.EMAIL_HOST_USER,[profile.user.email],fail_silently=False)
       
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
        send_mail("Booking rejected","Your booking was rejected",settings.EMAIL_HOST_USER,[profile.user.email],fail_silently=False)
        return Response({
            "message":"Booking deleted",
        },status=status.HTTP_200_OK)



@api_view(['GET'])
def query_bookings(request,profile_id):        
        profile = Profile.objects.get(id=profile_id)
        if profile.role != "RECEPTIONIST":
            return Response({"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
        
        pending_bookings = Booking.objects.filter(status="PENDING")
        approved_bookings = Booking.objects.filter(status="APPROVED")
        rejected_bookings = Booking.objects.filter(status="REJECTED")

        pending_serialized_bookings = BookingSerializer(pending_bookings,many=True).data
        approved_serialized_bookings = BookingSerializer(approved_bookings,many=True).data
        rejected_serialized_bookings = BookingSerializer(rejected_bookings,many=True).data
        bookings = {
            "rejecteds":rejected_serialized_bookings,
            "approveds":approved_serialized_bookings,
            "pendings":pending_serialized_bookings
        }
        return Response(bookings,status=status.HTTP_200_OK)    