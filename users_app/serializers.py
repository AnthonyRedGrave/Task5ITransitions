from rest_framework import serializers
from .models import UserProfile, User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'