from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.add_cart, name='add_cart'),
    path('pay/', views.pay, name='pay'),
]