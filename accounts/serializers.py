from django.contrib.auth import get_user_model
from rest_framework import serializers



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, read_only=True)
    nickname = serializers.CharField(max_length=20, read_only=True)
    profile = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class UserImgSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, read_only=True)
    img = serializers.ImageField()

    class Meta:
        model = User
        fields = '__all__'