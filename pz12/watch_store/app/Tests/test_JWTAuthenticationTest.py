from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class JWTAuthenticationTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/login/'  # Используйте относительный URL
        self.username = 'manger2'
        self.password = '123qweAS'
        User.objects.create_user(username=self.username, password=self.password)

    def test_jwt_authentication(self):
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_jwt_invalid_credentials(self):
        self.password = "WrongPassword"
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('Не найдено активной учетной записи с указанными данными', str(response.data))

