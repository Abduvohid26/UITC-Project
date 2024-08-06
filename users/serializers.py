from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'password'
        )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False}
        }

    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        user.save()
        return user

    def validate(self, attrs):
        username = attrs.get('username')
        if username and User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username already exists'})
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'image',
        )
        extra_kwargs = {
            'image': {'required': False},
        }


class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()


