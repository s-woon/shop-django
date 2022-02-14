from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
import json
import requests
from cart.models import CartItem
from product.models import Product
from order.models import Order
from django.db.models import Max

# Create your views here.


def kakaopay(request, uid, amount=0, totalQuantity=0):
    cartitem = CartItem.objects.filter(user_id=uid)
    order = Order()
    items = []
    # 총합가격
    for subtotal in cartitem:
        amount += (subtotal.product.price * subtotal.quantity)
    # 총합갯수
    for subtotal in cartitem:
        totalQuantity += subtotal.quantity
    # 상품명
    for item in cartitem:
        items.append(item.product.name)

    try:
        id = order.objects.latest('id')
    except:
        id = 0

    partner_order_id = id + 1

    cartItemsName = ""
    for i in items:
        cartItemsName += i + ', '


    url = 'https://kapi.kakao.com/v1/payment/ready'
    headers = {
        'Authorization': 'KakaoAK ',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    data = {
        'cid': "TC0ONETIME",
        'partner_order_id': partner_order_id,
        'partner_user_id': cartitem[0].user.username,
        'item_name': cartItemsName,
        'quantity': totalQuantity,
        'total_amount': amount,
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

    # DB 저장
    for i in range(len(items)):
        order.partner_order_id = partner_order_id
        order.tid = request.session['tid']
        order.user = cartitem[i].user
        order.product = cartitem[i].product
        order.quantity = cartitem[i].quantity
        order.amount = amount
        order.save()
    return redirect(next_url)


def kakaosuccess(request):
    print(request.session)
    order = Order.objects.get(tid=request.session['tid'])
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK ",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",  # 테스트용 코드
        # "tid": order.tid,
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": order.partner_order_id,  # 주문번호
        "partner_user_id": order.user.username,  # 유저 아이디
        "pg_token": request.GET.get("pg_token"),  # 쿼리 스트링으로 받은 pg토큰
    }
    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    cartitem = CartItem.objects.filter(user_id=order.user)
    cartitem.delete()
    return render(request, 'kakaopay/success.html', context)


def kakaocancel(request):
    return render(request, 'kakaopay/cancel.html')


def kakaofail(request):
    return render(request, 'kakaopay/fail.html')


def naverpay(request):
    pass


def cardpay(request):
    pass


