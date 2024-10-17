from parso.python.tree import Class
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone_number', 'inn']  # Укажите нужные поля

    extra_kwargs = {
        'password': {'write_only': True, 'required': True},  # Пароль должен быть только для записи
        'username': {'required': True},
        'email': {'required': True},
        'phone_number': {'required': True},
        'inn': {'required': True}
    }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            inn=validated_data['inn']
        )
        user.set_password(validated_data['password'])  # Хранение пароля в зашифрованном виде
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    extra_kwargs = {
        'name': {'required': True},
        'description': {'required': True},
        'price': {'required': True},
        'image': {'required': True},
        'stock': {'required': True},
    }
    def create(self, validated_data):
        product = Product(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            image=validated_data['image']
        )

        product.save()
        return product

