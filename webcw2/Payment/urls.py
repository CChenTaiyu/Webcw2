"""Payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Api.views import Signup, Signin, Transfer, Deposit, Balance, Payment_Order, Payment_Information, Statement, Payment_Check, Payment_Return

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Payment_WS/signup/', Signup),
    path('Payment_WS/signin/', Signin),
    path('Payment_WS/deposit/', Deposit),
    path('Payment_WS/balance/', Balance),
    path('Payment_WS/transfer/', Transfer),
    path('Payment_WS/statement/', Statement),
    path('Payment_WS/Payment Order/', Payment_Order),
    path('Payment_WS/Payment Information/', Payment_Information),
    path('Payment_WS/Payment Check/', Payment_Check),
    path('Payment_WS/Payment Return/', Payment_Return),
]
