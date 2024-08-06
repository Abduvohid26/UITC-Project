from django.shortcuts import render, get_object_or_404
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer, ResetPasswordSerializer
from rest_framework import generics, permissions, status
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(
                data={
                    'id': user.id,
                    'username': user.username,
                    'full_name': user.full_name,
                    'access_token': user.token()['access'],
                    'refresh_token': user.token()['refresh'],
                    'image': user.image.url
                }
            )
        return Response(
            {
                'success': False,
                'data': 'username or password invalid'
            }, status=status.HTTP_200_OK
        )


class UsersView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(instance=user, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UsersDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = get_object_or_404(User, id=id)
        except Exception as e:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found',
                    'error': {e}
                }
            )
        user.delete()
        return Response(
            data={
                'success': True,
                'code': 200,
                'message': 'User successfully deleted'
            }
        )


class ResetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            user = request.user
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response(
                    data={
                        'success': True,
                        'message': 'Password successfully updated'
                    }, status=status.HTTP_200_OK
                )
            return Response(
                data={
                    'success': False,
                    'message': "Incorrect old password"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)