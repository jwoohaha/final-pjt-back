from rest_framework import generics
from .serializers import UserSerializer

class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer