from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def pay(request):
    print(request.body)
    jsonObject = json.loads(request.body)

    context = {
        'result' : jsonObject,
    }
    return JsonResponse(context)