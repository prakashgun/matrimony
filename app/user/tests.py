from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class Utilities:
    CREATE_USER_URL = reverse

    @staticmethod
    def create_user(**params):
        return get_user_model().objects.create(**params)


class UserPublicApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test create user with payload"""
        res = self.client.post(
            Utilities.CREATE_USER_URL,
            {
                'username': 'test@example.com',
                'password': 'test',
                'name': 'Test Name'
            }
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
