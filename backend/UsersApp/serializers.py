from rest_framework import serializers
from .models import Booking, User , Profile

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Booking
        

        
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        fields = "__all__"
        model = User 
        
    def get_profile(self,obj):
        try:
            profile = Profile.objects.get(user=obj)
            return {
                "role":profile.role,
                "id":profile.id
            }
        except:
            return None