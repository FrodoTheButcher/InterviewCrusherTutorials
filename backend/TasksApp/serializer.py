from .models import Task 
from rest_framework import serializers
from UsersApp.serializers import UserSerializer, User,RoomSerializer

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    class Meta:
        model = Task 
        fields = "__all__"
        
    def get_user(self,obj):
        user =  obj.user 
        return UserSerializer(user,many=False).data
    def get_room(self,obj):
        room = obj.room 
        return RoomSerializer(room,many=False).data