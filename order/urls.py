from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'order'

urlpatterns = [
    path('kakaopay/<int:uid>/', views.kakaopay, name='kakaopay'),
    path('kakaopay/success/', views.kakaosuccess, name='kakaosuccess'),
    path('kakaopay/cancel/', views.kakaocancel, name='kakaocancel'),
    path('kakaopay/fail/', views.kakaofail, name='kakaofail'),

    path('naverpay/', views.naverpay, name='naverpay'),
    path('cardpay/', views.cardpay, name='cardpay'),
]
