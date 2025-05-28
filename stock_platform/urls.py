from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    #path('', lambda request: redirect('tab_dividend')),
    path('', lambda request: HttpResponse("OK")),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('stocks/', include('stocks.urls')),
]
