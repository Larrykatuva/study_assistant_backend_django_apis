from .test_setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestUserViews(TestSetup):

    def test_can_not_register_user_without_data(self):
        user = self.client.post(self.register_url)
        self.assertEqual(user.status_code, 400)

    def test_can_register_user_with_data(self):
        user = self.client.post(self.register_url, self.register_data)
        self.assertEqual(user.status_code, 201)

    def test_can_not_login_user_without_data(self):
        user = self.client.post(self.login_url)
        self.assertEqual(user.status_code, 400)

    def test_can_not_login_user_with_invalid_details(self):
        invalid_details = {'username': 'katuva', 'password': 'qazwsxedc'}
        user = self.client.post(self.login_url, invalid_details)
        self.assertEqual(user.status_code, 400)

    # def test_can_login_user_with_valid_details(self):
    #     self.client.post(self.register_url, self.register_data)
    #     user = self.client.post(self.login_url, self.register_data)
    #     self.assertEqual(user.status_code, 400)

    def test_can_complete_user_details(self):
        user = self.client.post(self.register_url, self.register_data)
        owner = user.data.get('id')
        details = {
          "first_name": "lawrence",
          "last_name": "katuva",
          "education_level": "Graduate",
          "date_of_birth": "15-08-1998",
          "country": "Kenya",
          "institution": "Kenyatta University",
          "field": "Computer science",
          "owner": owner
        }
        complete = self.client.post(self.complete_profile_url, details)
        self.assertEqual(complete.status_code, 200)

    def test_can_get_profile_by_id(self):
        user = self.client.post(self.register_url, self.register_data)
        owner = user.data.get('id')
        details = {
            "first_name": "lawrence",
            "last_name": "katuva",
            "education_level": "Graduate",
            "date_of_birth": "15-08-1998",
            "country": "Kenya",
            "institution": "Kenyatta University",
            "field": "Computer science",
            "owner": owner
        }
        complete = self.client.post(self.complete_profile_url, details)
        found = self.client.get(reverse('profile', args=[complete.data.get('id')]))
        self.assertEqual(found.status_code, 200)

    def test_can_update_profile(self):
        user = self.client.post(self.register_url, self.register_data)
        owner = user.data.get('id')
        details = {
            "first_name": "lawrence",
            "last_name": "katuva",
            "education_level": "Graduate",
            "date_of_birth": "15-08-1998",
            "country": "Kenya",
            "institution": "Kenyatta University",
            "field": "Computer science",
            "owner": owner
        }
        complete = self.client.post(self.complete_profile_url, details)
        update = {'education_level': 'Post Graduate'}
        found = self.client.patch(reverse('profile', args=[complete.data.get('id')]), update)
        self.assertEqual(found.status_code, 200)

    def test_can_get_user_profile(self):
        user = self.client.post(self.register_url, self.register_data)
        owner = user.data.get('id')
        details = {
            "first_name": "lawrence",
            "last_name": "katuva",
            "education_level": "Graduate",
            "date_of_birth": "15-08-1998",
            "country": "Kenya",
            "institution": "Kenyatta University",
            "field": "Computer science",
            "owner": owner
        }
        self.client.post(self.complete_profile_url, details)
        profile = self.client.get(reverse('user-profile', args=[owner]))
        self.assertEqual(profile.status_code, 200)