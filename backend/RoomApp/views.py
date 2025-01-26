# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from RoomApp.models import Room
from .serializers import RoomSerializer
from .requests import CreateRoomRequest
# Create your views here.

class RegisterRoomView(APIView):
    @swagger_auto_schema(request_body=CreateRoomRequest)
    def post(self, request):
        floor = request.data.get("floor")
        room_type = request.data.get("type")
        Room.objects.create(floor=floor, type=room_type, available=True)
        return Response(data="Room registered successfully", status=status.HTTP_201_CREATED)
    
    def get(self,request):
        rooms = Room.objects.all()
        print("oooms",rooms)
        serialized = RoomSerializer(rooms,many=True).data 
        print("serialized",serialized)
        return Response(data=serialized,status=status.HTTP_200_OK)