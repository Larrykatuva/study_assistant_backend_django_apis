from rest_framework.test import APITestCase
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register-user')
        self.login_url = reverse('login-user')
        self.activate_url = reverse('activate-user')
        self.complete_profile_url = reverse('complete-profile')

        self.register_data = {
            'username': 'string',
            'email': 'string@gmail.com',
            'password': 'string'
        }

        self.login_data = {
            'username': 'string',
            'password': 'string'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()