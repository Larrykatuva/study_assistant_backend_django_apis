from src.serializers.authentication.authentication_serializers import RegisterSerializer, UserSerializer, \
    LoginSerializer, LoginResponseSerializer, ActivateSerializer, CompleteProfileSerializer, \
    UpdateProfileSerializer, ProfileSerializerReadonly
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from src.services.authentication.user_service import UserService
from src.services.authentication.profile_service import ProfileService
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    user_service = UserService()

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            res = self.user_service.create_user(request, data.get('username'), data.get('email'), data.get('password'))
            self.serializer_class = UserSerializer
            serialized_data = self.serializer_class(res)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    user_service = UserService()

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            res = self.user_service.login_user(data.get('username'), data.get('password'))
            self.serializer_class = LoginResponseSerializer
            serialized_data = self.serializer_class(res)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class ActivateAPIView(GenericAPIView):
    serializer_class = ActivateSerializer
    user_service = UserService()

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            res = self.user_service.activate_user(request, data.get('code'))
            self.serializer_class = UserSerializer
            serialized_data = self.serializer_class(res)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class CompleteProfileAPIView(GenericAPIView):
    serializer_class = CompleteProfileSerializer
    user_service = UserService()
    profile_service = ProfileService()

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            self.user_service.update_user(id=data.get('owner'), first_name=data.get('first_name'),
                                          last_name=data.get('last_name'))
            user = self.user_service.get_user_by_id(data.get('owner'))
            self.profile_service.create_profile(image=data.get('image'),
                                                education_level=data.get('education_level'),
                                                date_of_birth=data.get('date_of_birth'),
                                                country=data.get('country'), institution=data.get('institution'),
                                                field=data.get('field'), owner=user)
            self.serializer_class = ProfileSerializerReadonly
            profile = self.profile_service.get_user_profile(data.get('owner'))
            serialized_data = self.serializer_class(profile)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateProfileSerializer
    profile_service = ProfileService()
    queryset = profile_service.get_all_profiles()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()


class UserProfileAPIView(GenericAPIView):
    serializer_class = ProfileSerializerReadonly
    profile_service = ProfileService()

    def get(self, request, id):
        profile = self.profile_service.get_user_profile(id)
        serialized_data = self.serializer_class(profile)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

