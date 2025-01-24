from rest_framework import serializers

class CreateUserRequest(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    
class CreateRoomRequest(serializers.Serializer):
    floor= serializers.IntegerField()
    type = serializers.CharField()
    
class RegisterUserAndMakeBookingRequest(serializers.Serializer):
    email = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    room_id = serializers.IntegerField()