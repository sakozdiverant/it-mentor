from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ..models import Product, Cart, CartItem, User


class CartViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='Testpass123!')
        self.client.force_authenticate(user=self.user)

        self.product1 = Product.objects.create(name='Test Product 1', description='Description 1', price=100)
        self.product2 = Product.objects.create(name='Test Product 2', description='Description 2', price=200)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item1 = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart, product=self.product2, quantity=3)

        self.url = '/api/cart/'

    def test_view_cart(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 2)
        self.assertEqual(response.data['items'][0]['product']['name'], 'Test Product 1')
        self.assertEqual(response.data['items'][1]['product']['name'], 'Test Product 2')
