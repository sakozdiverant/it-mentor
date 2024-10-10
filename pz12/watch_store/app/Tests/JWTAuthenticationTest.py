from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class JWTAuthenticationTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='123qweAS')
        self.url = '/api/token/'
        self.data = {
            'username': 'testuser',
            'password': '123qweAS'
        }

    def test_jwt_authentication(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_jwt_invalid_credentials(self):
        self.data['password'] = 'WrongPass'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('No active account found', str(response.data))
