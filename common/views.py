from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from common.forms import UserForm
# Create your views here.
import requests
import json
from django.contrib.auth import models


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('product:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def kakao_login(request):
    CLIENT_ID = "ae9d5bd57e76f978a74ff65c633debf9"
    REDIRET_URL = "http://localhost:8080/common/login/kakao/callback/"
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
        CLIENT_ID, REDIRET_URL)
    res = redirect(url)
    return res


def kakao_login_callback(request):
    CODE = request.GET.get('code')
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': "ae9d5bd57e76f978a74ff65c633debf9",
        'redirect_url': "http://localhost:8080/common/login/kakao/callback/",
        'code': CODE,
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    token_response = requests.post(kakao_token_api, data=data, headers=headers)

    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})
    user_data = user_info_response.json()

    email = user_data['kakao_account']['email']
    username = user_data['properties']['nickname']

    user = User.objects.filter(email=email).first()

    if not user:
        user = User.objects.create_user(
            email=email,
            username=username
        )
        user.set_unusable_password()
        user.save()

        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

    else:
        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

    return redirect('/')

    # return render(request, 'common/login.html')
    # return JsonResponse({"user_info": user_info_response.json()})