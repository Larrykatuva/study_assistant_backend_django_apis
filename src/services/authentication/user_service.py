from django.contrib.auth.models import User
from src.errors.authentication.authentication_errors import AuthenticationErrors
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from random import randrange
from src.utils.email import Email


class UserService:

    def __init__(self):
        self.auth_errors = AuthenticationErrors()

    @staticmethod
    def get_user_by_username(username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_id(id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def generate_random_code():
        return str(randrange(10)) + "" + str(randrange(10)) + "" + str(randrange(10)) + "" + str(randrange(10))

    def read_activation_code(self, request, code):
        try:
            return request.session[str(code)]
        except Exception as err:
            raise Exception(self.auth_error.raise_activation_code_expired())

    def create_user(self, request, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()
        self.send_activation_email(request,email, user.id)
        return user

    def send_activation_email(self, request,email, user_id):
        activate_code = self.generate_random_code()
        email_subject = 'Activate your Account'
        email_body = 'Your activation code is ' + activate_code
        Email.send(email_subject, email_body, [email])
        request.session[activate_code] = user_id

    def activate_user(self, request, code):
        user_id = request.session[code]
        user = self.get_user_by_id(user_id)
        user.is_active = True
        user.save()
        return user

    @staticmethod
    def generate_auth_tokens(user):
        tokens = RefreshToken.for_user(user)
        return {
            'refresh': str(tokens),
            'access': str(tokens.access_token)
        }

    def login_user(self, username, password):
        found = self.get_user_by_username(username)
        if not found:
            raise AuthenticationFailed(self.auth_errors.raise_username_does_not_exist())
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed(self.auth_errors.raise_auth_failed())
        token = self.generate_auth_tokens(user)
        print(token)
        return {
            'user': user,
            'token': token
        }

    @staticmethod
    def update_user(id, **kwargs):
        return User.objects.filter(pk=id).update(**kwargs)
