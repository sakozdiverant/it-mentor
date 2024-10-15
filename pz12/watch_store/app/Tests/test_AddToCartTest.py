from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Cart, CartItem, Product
from rest_framework_simplejwt.tokens import AccessToken


class CartTests(APITestCase):

    def authenticate(self):
        # Устанавливаем токен в заголовок авторизации
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='manger2', password='123qweAS')
        self.product = Product.objects.create(name='Test Product', description='Test description', price=2.00, stock=2)
        self.token = str(AccessToken.for_user(self.user))
        self.url = '/api/cart/add/'
        self.data = {
            #'Authorization': self.token,
            'product_id': self.product.id,
            'quantity': 2
        }

    def test_add_product_to_cart(self):
        self.authenticate()
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(CartItem.objects.filter(cart__user=self.user, product=self.product).exists())

    def test_invalid_product_id(self):
        self.authenticate()
        self.data['product_id'] = 999  # Несуществующий продукт
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Продукт с таким ID не существует', str(response.data))
