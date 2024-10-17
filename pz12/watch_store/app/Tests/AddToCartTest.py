from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Cart, CartItem, Product
from rest_framework_simplejwt.tokens import AccessToken


class CartTests(APITestCase):

    def authenticate(self):

        self.username = 'manger2'
        self.password = '123qweAS'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/cart/add/'
        self.data = {

            'product_id': 2,
            'quantity': 2
        }

    def test_add_product_to_cart(self):
        self.authenticate()

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Product added to cart', str(response.data))



    def test_invalid_product_id(self):
        self.authenticate()
        self.data['product_id'] = 999  # Несуществующий продукт
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Продукт с таким ID не существует.', str(response.data))
