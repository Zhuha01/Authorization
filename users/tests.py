from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class AuthAPITests(APITestCase):
    # Test cases for authentication API

    def setUp(self):
        # Prepare URLs and initial user for tests
        self.register_url = reverse('auth_register')
        self.login_url = reverse('rest_login')

        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'a-very-strong-password123',
        }

        # Create initial user
        self.user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )

    def test_user_registration_success(self):
        # Test successful registration
        payload = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': self.user_data['password'],
            'password2': self.user_data['password'],
        }
        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.latest('id').username, 'newuser')

    def test_user_registration_failure_password_mismatch(self):
        # Test registration fails when passwords do not match
        payload = {
            'username': 'anotheruser',
            'email': 'another@example.com',
            'password': 'password123',
            'password2': 'password456',
        }
        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login_success(self):
        # Test successful login
        payload = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }
        response = self.client.post(self.login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_failure_wrong_password(self):
        # Test login fails with wrong password
        payload = {
            'email': self.user_data['email'],
            'password': 'this-is-the-wrong-password',
        }
        response = self.client.post(self.login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
