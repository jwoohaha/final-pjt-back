from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.response import Response

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    if request.method == 'PUT':
        username = request.data.get('username')
        new_nickname = request.data.get('nickname')
        new_profile = request.data.get('profile')
        new_profile_img = request.data.get('profile_img')

        User = get_user_model()
        user = get_object_or_404(User, username=username)

        # 토큰 인증을 위해 request.user를 사용하여 현재 사용자를 가져올 수 있습니다.
        # request.user는 인증된 사용자 객체입니다.
        if request.user == user:
            user.nickname = new_nickname
            user.profile = new_profile
            user.profile_img = new_profile_img
            user.save()
            return HttpResponse('Good boy!', status=200)  # 잘해썽 요청 응답

    elif request.method == 'GET':
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    return HttpResponse('Invalid request', status=400)  # 잘못된 요청 응답

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    print(user)
    print('user_id:', user.id)
    return Response({'user_id': user.id})
