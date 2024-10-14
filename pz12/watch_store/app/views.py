from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProductSerializer, CartSerializer, AddToCartSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .models import Product, Cart, CartItem
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Регистрация пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Вход пользователя (получение токенов)
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

# Обновление токена
class RefreshTokenView(TokenRefreshView):
    permission_classes = (AllowAny,)

# Список продуктов
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort', 'name')
        if sort_by not in ['name', '-name', 'price', '-price', 'id', '-id']:
            sort_by = 'name'
        return Product.objects.all().order_by(sort_by)

# Поиск продуктов по названию
class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        query = self.request.query_params.get('name', '')
        return Product.objects.filter(name__icontains=query)

# Сортировка продуктов
class ProductSortedView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort', 'name')
        if sort_by not in ['name', '-name', 'price', '-price']:
            sort_by = 'name'
        return Product.objects.all().order_by(sort_by)

# Добавление продукта в корзину
class AddToCartView(APIView):
    permission_classes = (IsAuthenticated,)  # Требуется аутентификация

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            # Получаем продукт
            product = get_object_or_404(Product, id=product_id)

            # Получаем корзину пользователя или создаем новую
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Проверяем, есть ли этот товар в корзине
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            if not created:  # Если товар уже есть в корзине, обновляем количество
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()  # Сохраняем изменения

            return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Просмотр корзины
class CartView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return Response({"message": "Корзина успешно создана"
        if created else "Корзина уже существует"}, status=status.HTTP_200_OK)


    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"message": "Корзина пуста"}, status=status.HTTP_200_OK)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Оформление заказа (простой пример)
class CheckoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            if not cart.cartitem_set.exists():
                return Response({"message": "Корзина пуста"}, status=status.HTTP_400_BAD_REQUEST)
            # Здесь можно добавить логику создания заказа
            # Например, создание объекта Order и копирование данных из корзины
            # Для простоты просто очищаем корзину
            cart.cartitem_set.all().delete()
            return Response({"message": "Заказ оформлен"}, status=status.HTTP_201_CREATED)
        except Cart.DoesNotExist:
            return Response({"message": "Корзина пуста"}, status=status.HTTP_400_BAD_REQUEST)
