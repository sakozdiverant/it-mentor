from rest_framework import generics, status
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Product, Cart, CartItem


class CartApiList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CartApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    #permission_classes = (IsOwnerOrReadOnly,)

class CartApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CartItemApiList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer

class CartItemUpdate(generics.RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    #permission_classes = (IsOwnerOrReadOnly,)

class CartItemDestroy(generics.RetrieveDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminOrReadOnly,)

class CustomUserApiList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CartSerializer
    #permission_classes = ()

class CustomUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CartSerializer
    permission_classes = (AllowAny,)

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        Cart.objects.create(user=user)

class CustomUserDestroy(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminOrReadOnly,)

class ProductApiList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = (IsOwnerOrReadOnly,)

class ProductDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
