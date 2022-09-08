from rest_framework import serializers
from data_app.models import UserProfile, UserAddress


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user_id", "first_name", "last_name", "phone"]


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ["user_id", "address"]
