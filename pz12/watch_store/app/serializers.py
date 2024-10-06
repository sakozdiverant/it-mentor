# app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator



class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)  # Поле для подтверждения пароля
    inn = serializers.CharField(max_length=12, min_length=12, required=True, write_only=True)
    phone_number = serializers.CharField(max_length=15, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'inn', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Проверка совпадения паролей
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        # Удаляем поле password2 из validated_data, так как оно не нужно для создания пользователя
        validated_data.pop('password2')

        # Сохраняем данные профиля
        inn = validated_data.pop('inn')
        phone_number = validated_data.pop('phone_number')

        # Создаем пользователя
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Создаем или обновляем профиль пользователя
        Profile.objects.update_or_create(
            user=user,
            defaults={
                'inn': inn,
                'phone_number': phone_number
            }
        )

        return user

# Сериализатор для продуктов
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

# Сериализатор для элементов корзины
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

# Сериализатор для корзины
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']

# Сериализатор для добавления товара в корзину
class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    def validate_product_id(self, value):
        # Проверяем, существует ли продукт с указанным ID
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Продукт с таким ID не существует.")
        return value

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество должно быть минимум 1.")
        return value

    def validate(self, data):
        # Получаем пользователя из контекста
        user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError("Пользователь не аутентифицирован.")

        # Проверяем, что корзина пользователя существует
        if not Cart.objects.filter(user=user).exists():
            raise serializers.ValidationError("Корзина пользователя не найдена.")

        return data

    def save(self):
        # Получаем пользователя из контекста
        user = self.context['request'].user
        cart = Cart.objects.get(user=user)  # Получаем корзину пользователя

        # Получаем продукт и количество из валидированных данных
        product = Product.objects.get(id=self.validated_data['product_id'])
        quantity = self.validated_data['quantity']

        # Добавляем товар в корзину или обновляем его количество
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return cart_item