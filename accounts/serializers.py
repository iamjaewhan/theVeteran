from .models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_id = serializer.CharField(max_length=50)