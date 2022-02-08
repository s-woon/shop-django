from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_add/', views.add_cart, name='add_cart'),
    path('cart_update/', views.update_cart, name='update_cart'),
    path('cart_delete/', views.delete_cart, name='delete_cart'),
    path('cart_delete_all/', views.delete_all_cart, name='delete_all_cart'),
    path('', views.cart, name='cart'),
]