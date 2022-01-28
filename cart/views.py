from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
# Create your views here.
import requests

# product = Product.objects.get(id=jsonObject.order_pro_id)
def cart(request):
    print(request)
    print("여기", request.body)
    jsonObject = json.loads(request.body)
    context = { "jsonObject" : jsonObject}
    print(context)
    return JsonResponse(context)
# {"ffff":"ccccc"}

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


