from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from cart.models import CartItem
from product.models import Product
import requests


# @login_required(login_url='common:login')
def add_cart(request):
    cart = CartItem()
    jsonObject = json.loads(request.body)
    # DB에 그냥 계속 추가되는 오류수정하기 위해
    # cart.user html에서 유저 id값도 던져서 id값 검사 후
    cart.product = Product.objects.get(id=jsonObject["order_pro_id"])
    cart.quantity = int(jsonObject["order_quantity"])
    cart.save()
    return JsonResponse(jsonObject)


def pay(request):

    return render(request, 'cart/cart.html')

# window.location.href= "/cart/pay/";

# @csrf_exempt
# def add_cart(request):
#
#     jsonObject = json.loads(request.body)
#
#     url = "127.0.0.1:8080/cart/add_cart/"
#     order_pro_id = jsonObject.get('order_pro_id', None)
#     order_quantity = jsonObject.get('order_quantity', None)
#
#     context = {
#         'order_pro_id' : order_pro_id,
#         'order_quantity' : order_quantity
#     }
#
#     print(context)
#     # context = {
#     #     'result': jsonObject,
#     # }
#
#     # return JsonResponse(context)
#     return render(request, 'cart/cart.html', context)


