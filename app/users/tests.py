from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class Utilities:
    CREATE_USER_URL = reverse('users:create')

    @staticmethod
    def create_user(**params):
        return get_user_model().objects.create(**params)


class ModelTests(TestCase):

    def test_create_user_successful(self):
        username = '9876543210'
        password = 'test'
        email = 'test@example.com'

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_new_user_invalid_email(self):
    #     """Test creating user with invalid email raises error"""
    #     username = '9876543210'
    #     password = 'test'
    #     email = 'test'
    #
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user(username=username,
    #                                              password=password,
    #                                              email=email)


class UserPublicApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test create user with payload"""
        payload = {
            'username': '9876543210',
            'password': 'test',
            'email': 'test@example.com'
        }

        res = self.client.post(Utilities.CREATE_USER_URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_unique_email(self):
        """Test user cannot be created with already existing email"""
        payload = {
            'username': '9876543210',
            'password': 'test',
            'email': 'test@example.com'
        }

        Utilities.create_user(**payload)

        payload = {
            'username': '9976543210',
            'password': 'test2',
            'email': 'test@example.com'
        }

        res = self.client.post(Utilities.CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_username(self):
        """Validate that username is ten digit"""
        payload = {
            'username': '987654321',  # 9 digit number
            'password': 'test',
            'email': 'test@example.com'
        }

        res = self.client.post(Utilities.CREATE_USER_URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_email(self):
        """Validate that username is ten digit"""
        payload = {
            'username': '9876543210',
            'password': 'test',
            'email': 'wrong_email'
        }

        res = self.client.post(Utilities.CREATE_USER_URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
