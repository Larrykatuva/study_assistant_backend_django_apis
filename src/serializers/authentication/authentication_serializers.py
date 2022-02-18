from django.contrib.auth.models import User
from rest_framework import serializers
from src.models.authentication_models import Profile


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    class Meta:
        fields = ['username', 'password']


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=1000)
    access = serializers.CharField(max_length=1000)

    class Meta:
        fields = ['refresh', 'access']


class LoginResponseSerializer(serializers.Serializer):
    user = UserSerializer()
    token = TokenSerializer()

    class Meta:
        fields = ['user', 'token']


class ActivateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, min_length=4, required=True)

    class Meta:
        fields = ['code']


class CompleteProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'education_level', 'date_of_birth', 'country', 'institution', 'field', 'owner']


class ProfileSerializer:
    pass


class ProfileSerializerReadonly(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'is_writer', 'is_account', 'is_admin', 'is_superuser', 'image', 'education_level',
                  'date_of_birth', 'country', 'institution', 'certificate', 'field', 'owner']


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'is_writer', 'is_account', 'is_admin', 'is_superuser', 'image', 'education_level', 'date_of_birth', 'country', 'institution', 'field', 'owner']

