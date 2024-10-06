# app/urls.py
from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView, ProductListView, ProductSearchView, ProductSortedView, \
    AddToCartView, CartView, CheckoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),


    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/sorted/', ProductSortedView.as_view(), name='product-sorted'),

    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    # Используем POST с product_id и quantity в теле запроса
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
