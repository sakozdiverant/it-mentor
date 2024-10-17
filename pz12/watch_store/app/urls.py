# app/urls.py
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('cart/', CartApiList.as_view(), name='cart'),
    path('cart/<int:pk>', CartApiUpdate.as_view(), name='CartApiUpdate'),
    path('cart/delete/<int:pk>',CartApiDestroy.as_view(), name='CartApiDestroy'),
    path('cartitem/', CartItemApiList.as_view(), name='CartItemApiList'),
    path('cartitem/<int:pk>', CartItemUpdate.as_view(), name='CartItemUpdate'),
    path('cartitem/delete/<int:pk>', CartItemDestroy.as_view(), name='CartItemDestroy'),
    path('login/', CustomUserApiList.as_view(), name='CustomUserCreate'),
    path('register/', CustomUserCreate.as_view(), name='CustomUserCreate'),
    path('login/<int:pk>', CustomUserUpdate.as_view(), name='CustomUserUpdate'),
    path('login/delete/<int:pk>', CustomUserDestroy.as_view(), name='CustomUserDestroy'),
    path('product/', ProductApiList.as_view(), name='ProductApiList'),
    path('product/creat/', ProductCreateAPIView.as_view(), name='ProductCreateAPIView'),
    path('product/<int:pk>', ProductUpdate.as_view(), name='ProductUpdate'),
    path('product/delete/<int:pk>', ProductDestroy.as_view(), name='ProductDestroy'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
