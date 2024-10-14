from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ..models import Product, Cart, CartItem, User


class AddToCartTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'manger2'
        self.password = '123qweAS'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)


        self.url = '/api/cart/add/'
        self.data = {
            'product_id': 3,
            'quantity': 2
        }

    def test_add_product_to_cart(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(CartItem.objects.filter(cart__user=self.user, product=self.product).exists())

    def test_invalid_product_id(self):
        self.data['product_id'] = 999  # Несуществующий продукт
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Продукт с таким ID не существует', str(response.data))
