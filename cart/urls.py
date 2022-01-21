from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('pay/', views.pay, name='pay'),
]