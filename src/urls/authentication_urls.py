from django.urls import path
from src.views.authentication_view import RegisterAPIView, LoginAPIView, \
    ActivateAPIView, CompleteProfileAPIView, UpdateProfileAPIView, UserProfileAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register-user'),
    path('login', LoginAPIView.as_view(), name='login-user'),
    path('activate', ActivateAPIView.as_view(), name='activate-user'),
    path('complete-profile', CompleteProfileAPIView.as_view(), name="complete-profile"),
    path('profile/<id>', UpdateProfileAPIView.as_view(), name='profile'),
    path('profile/user/<id>', UserProfileAPIView.as_view(), name='user-profile')
]
