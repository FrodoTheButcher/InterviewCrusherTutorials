from rest_framework import serializers

class CreateRoomRequest(serializers.Serializer):
    floor= serializers.IntegerField()
    type = serializers.CharField()
    image = serializers.ImageField()
    name = serializers.CharField()
    description = serializers.CharField()