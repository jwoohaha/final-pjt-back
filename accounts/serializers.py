from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = '__all__'