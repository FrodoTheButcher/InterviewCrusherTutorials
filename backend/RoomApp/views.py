# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from RoomApp.models import Room
from .serializers import RoomSerializer
from .requests import CreateRoomRequest
from UsersApp.models import Profile , User
# Create your views here.

class RegisterRoomView(APIView):
    @swagger_auto_schema(request_body=CreateRoomRequest)
    def post(self, request):
        floor = request.data.get("floor")
        room_type = request.data.get("type")
        image = request.data.get("image")
        name = request.data.get("name")
        description = request.data.get("description")
        Room.objects.create(floor=floor, type=room_type, image=image,available=True,name=name,description=description)
        return Response(data="Room registered successfully", status=status.HTTP_201_CREATED)
    
    def get(self,request):
        rooms = Room.objects.all()
        print("oooms",rooms)
        serialized = RoomSerializer(rooms,many=True).data 
        print("serialized",serialized)
        return Response(data=serialized,status=status.HTTP_200_OK)
    
    
class DeleteRoomView(APIView):
    def delete(self,request,user_requesting,pk):
     user_requesting = User.objects.get(id=user_requesting)
     profile = Profile.objects.get(user=user_requesting)
     if profile.role != "MANAGER":
        return Response(status=status.HTTP_401_UNAUTHORIZED)
     room = Room.objects.get(id=pk)
     room.delete()
     return Response({"message":"Room deleted successfully"},status=status.HTTP_200_OK)
