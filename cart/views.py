from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from cart.models import CartItem
from product.models import Product
from django.views.generic import DetailView
import requests


def add_cart(request):
    cart = CartItem()
    jsonObject = json.loads(request.body)
    cart.user_id = request.user.id
    cart.product = Product.objects.get(id=jsonObject["order_pro_id"])
    cart.quantity = int(jsonObject["order_quantity"])
    cart.save()
    return HttpResponse("true", content_type='application/json')


@csrf_exempt
def update_cart(request):
    jsonObject = json.loads(request.body)
    cart_update = CartItem.objects.get(id=jsonObject["order_id"])
    cart_update.quantity = int(jsonObject["order_quantity"])
    cart_update.save()
    return HttpResponse("true", content_type='application/json')


@csrf_exempt
def delete_cart(request):
    jsonObject = json.loads(request.body)
    cart_delete = CartItem.objects.get(id=jsonObject["del_id"])
    cart_delete.delete()
    return HttpResponse("true", content_type='application/json')


@csrf_exempt
def delete_all_cart(request):
    jsonObject = json.loads(request.body)
    cart_delete = CartItem.objects.filter(user_id=jsonObject["del_userId"])
    print(cart_delete)
    cart_delete.delete()
    return HttpResponse("true", content_type='application/json')

def cart(request):
    model = CartItem.objects.filter(user_id=request.user.id)
    context = {
        'items': model,
    }
    return render(request, 'cart/cart_detail.html', context)

# window.location.href= "/cart/pay/";