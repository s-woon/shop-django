from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
import json
import requests
from cart.models import CartItem
from product.models import Product
# Create your views here.


def kakaopay(request, uid):
    cartitem = CartItem.objects.filter(user_id=uid)
    for item in cartitem:
        print(item.user)
        print(item.product)
        print(item.quantity)
    url = 'https://kapi.kakao.com/v1/payment/ready'
    headers = {
        'Authorization': 'KakaoAK ',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    data = {
        'cid': "TC0ONETIME",
        'partner_order_id': "1",
        'partner_user_id': "german",
        'item_name': "product",
        'quantity': 1,
        'total_amount': 100,
        'tax_free_amount': 0,
        'approval_url': 'http://127.0.0.1:8080/order/kakaopay/success/',
        'fail_url': 'http://127.0.0.1:8080/order/kakaopay/cancel/',
        'cancel_url': 'http://127.0.0.1:8080/order/kakaopay/fail/'
    }

    # 카카오응답
    response = requests.post(url, data=data, headers=headers)
    result = response.json()
    request.session['tid'] = result['tid']
    next_url = result['next_redirect_pc_url']
    return redirect(next_url)

    # return render(request, 'kakaopay/notpost.html')


def kakaosuccess(request):
    return render(request, 'kakaopay/success.html')


def kakaocancel(request):
    return render(request, 'kakaopay/cancel.html')


def kakaofail(request):
    return render(request, 'kakaopay/fail.html')


def naverpay(request):
    pass


def cardpay(request):
    pass

