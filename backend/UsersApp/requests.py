from rest_framework import serializers
from .models import Profile

class CreateUserRequest(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    image = serializers.ImageField()
    role = serializers.ChoiceField(choices = Profile.ROLE_CHOICES)
    
class BookingRequest(serializers.Serializer):
    email = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    room_id = serializers.IntegerField()