from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Room, Booking
from .requests import CreateUserRequest, CreateRoomRequest  # Ensure these are correctly imported

class RegisterRoomView(APIView):
    @swagger_auto_schema(request_body=CreateRoomRequest)
    def post(self, request):
        try:
            floor = request.data.get("floor")
            room_type = request.data.get("type")
            Room.objects.create(floor=floor, type=room_type, available=True)
            return Response(data="success")
        except Exception as e:
            return Response(data="fail", status=400)

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

class RegisterUserAndMakeBookingView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        user = User.objects.get(email=email)
        rooms = Room.objects.filter(available=True)

        if not rooms.exists():
            return Response("No available rooms.", status=404)

        room_id = request.query_params.get('room_id')
        selected_room = Room.objects.filter(id=room_id, available=True).first()

        if not selected_room:
            return Response("Invalid room selection or room not available.", status=400)

        start = request.query_params.get('start_date')
        end = request.query_params.get('end_date')

        booking = Booking.objects.create(
            room=selected_room,
            start_date=start,
            end_date=end,
            user=user
        )

        return Response({
            "message": "Booking successful",
            "details": {
                "user": user.email,
                "room_id": selected_room.id,
                "start_date": booking.start_date,
                "end_date": booking.end_date
            }
        })

