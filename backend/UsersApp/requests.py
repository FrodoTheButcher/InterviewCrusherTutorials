from rest_framework import serializers
from .models import Profile

class CreateUserRequest(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    image = serializers.CharField()
    role = serializers.ChoiceField(choices = Profile.ROLE_CHOICES)
    
class BookingRequest(serializers.Serializer):
    email = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    room_id = serializers.IntegerField()