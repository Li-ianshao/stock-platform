from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import logging

auth_logger = logging.getLogger('auth_logger')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            auth_logger.info(f"登入成功：{username}")
            return redirect('/stocks/dividend/')
        else:
            auth_logger.warning(f"登入失敗：{username}")
            messages.error(request, '帳號或密碼錯誤')
    return render(request, 'accounts/login.html')
