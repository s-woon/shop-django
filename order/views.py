from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
import json
# Create your views here.


# @csrf_exempt
# def cart(request):
#     jsonObject = json.loads(request.body)
#     context = {
#         'result' : jsonObject,
#     }
#     print(request)
#     print(request.body)
#     print(context)
#     return JsonResponse(context)

@csrf_exempt
def cart(request):
    jsonObject = json.loads(request.body)
    result = jsonObject
    print(result["order_pro_id"])
    return render(request, 'cart/cart.html', result)
    # return JsonResponse(result)

