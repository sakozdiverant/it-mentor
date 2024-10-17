from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class UserRegistrationTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/register/'
        self.data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': '123qweAS',
            'password2': '123qweAS',
            'inn': '123456789012',
            'phone_number': '877776667777'
        }

    def test_user_registration(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_password_mismatch(self):
        self.data['password2'] = 'wrongpassword'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Пароли не совпадают', str(response.data))
