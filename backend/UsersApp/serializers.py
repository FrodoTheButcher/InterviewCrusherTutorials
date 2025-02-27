from rest_framework import serializers
from .models import Booking, User , Profile , UserRegistrationRequest , Room
from RoomApp.serializers import RoomSerializer

class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserRegistrationRequest
class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = Booking
    def get_room(self,obj):
        try:
            room = obj.room
            return RoomSerializer(room).data
        except:
            return None
    def get_user(self,obj):
        try:
            user = obj.user
            return UserSerializer(user).data
        except Exception as e:
            print(e)
            return None  

        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Profile
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        fields = ['email','first_name','last_name','id','profile']
        model = User 
        
    def get_profile(self,obj):
        try:
            profile = Profile.objects.get(user=obj)
            
            return ProfileSerializer(profile,many=False).data
        except:
            return None