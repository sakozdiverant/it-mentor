from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ..models import Product, Cart, CartItem, User


class AddToCartTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='Testpass123!')
        self.client.force_authenticate(user=self.user)

        self.product = Product.objects.create(name='Test Product', description='Test Description', price=100)
        self.url = '/api/cart/add/'
        self.data = {
            'product_id': self.product.id,
            'quantity': 2
        }

    def test_add_product_to_cart(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(CartItem.objects.filter(cart__user=self.user, product=self.product).exists())

    def test_invalid_product_id(self):
        self.data['product_id'] = 9999  # Несуществующий продукт
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Продукт с таким ID не существует', str(response.data))
