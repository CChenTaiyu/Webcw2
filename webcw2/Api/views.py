from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import User, payRecord
from .serializers import UserSerializer
import json
from datetime import datetime
import secrets

# Create your views here.
# Sign up new user
def Signup(request):
        if request.method == "POST":
                user = json.loads(request.body)
                username = user["username"]
                password = user["password"]
                deposit = 500
                name = user["name"]
                user_exist = User.objects.filter(username = username)
                if len(user_exist) != 0:
                        return JsonResponse({"msg": "Username already exists."})
                new_user = User(username=username, password=password, deposit=deposit,
                                name=name)
                new_user.save()
                return JsonResponse({"msg": new_user.id})

def Signin(request):
        if request.method == "POST":
                user = json.loads(request.body)
                username = user["username"]
                password1 = user["password"]
                exist_user = User.objects.filter(username = username).first()
                if exist_user is None:
                        return JsonResponse({"msg": "You have no account, please sign up."})
                password2 = exist_user.password
                if password1 == password2:
                        return JsonResponse({"msg":exist_user.id})

def Deposit(request):
        if request.method == "POST":
                user = json.loads(request.body)
                userid = user["uid"]
                exist_user = User.objects.filter(id=userid).first()
                return JsonResponse({"msg": exist_user.deposit})

def Balance(request):
    if request.method == "POST":
        income = 0
        expense = 0
        user = json.loads(request.body)
        id = user["uid"]
        exist_user = User.objects.filter(id=id).first()
        Records = payRecord.objects.filter(userId=exist_user).all()
        for record in Records:
            if record.recipient == "income":
                income += record.money
            else:
                expense += record.money
        items = {"income": income, "expense": expense}
        # Convert the set items to a dictionary
        data = {"income": items.get("income"), "expense": items.get("expense")}
        # Return the JSON response
        return JsonResponse(data, safe=False)

def Transfer(request):
        if request.method == "POST":
                user = json.loads(request.body)
                userid = user["uid"]
                password = user["password"]
                username2 = user["u2"]
                username3 = user["u3"]
                money = user["money"]
                exist_user = User.objects.filter(id=userid).first()
                if password != exist_user.password:
                        return JsonResponse({"msg": "Wrong password."})
                if username2 != username3:
                        return JsonResponse({"msg": "Input different usernames for transfering. Please"
                                                                             "check"})
                another_user = User.objects.filter(username=username2).first()
                if another_user is None:
                        return JsonResponse({"msg": "We can not find the user with this username."})
                if exist_user.deposit < money:
                        return JsonResponse({"msg": "Insufficient deposit!"})
                exist_user.deposit -= money
                another_user.deposit += money
                exist_user.save()
                another_user.save()
                time = datetime.now()
                sk = secrets.token_hex(8)
                o_info1 = payRecord(time=time, recipient="expense", amount=1, money=money, secret_key=sk,
                                   userId=exist_user, airline_order=0, state=True)
                o_info2 = payRecord(time=time, recipient="income", amount=1, money=money, secret_key=sk,
                                   userId=another_user, airline_order=0, state=True)
                o_info1.save()
                o_info2.save()
                return JsonResponse({"msg": "Transfer successfully!"})

def Statement(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        main = req.get("uid") and len(req) == 1
        if main:
            uid = req["uid"]
        query_consumption = payRecord.objects.all()
        exist_user = User.objects.filter(id=uid).first()
        con = {}
        num = 0
        for i in query_consumption:
            if i.userId == exist_user:
                con1 = {"Time": i.time, "Money": i.money, "Recipient": i.recipient}
                con[num] = con1
                num += 1
        return JsonResponse({"msg": con})

def Payment_Information(request):
    if request.method == 'POST':
        order_id = None
        seat_price = None
        airline_name = None
        data = json.loads(request.body)
        flag = data.get("order_id") and data.get("seat_price") and data.get("air_name") and len(data) == 3
        if flag:
            order_id = data["order_id"]
            seat_price = data["seat_price"]
            airline_name = data["air_name"]
        time = datetime.now()
        sk = secrets.token_hex(8)
        o_info = payRecord(time=time, recipient="expense", amount=1, money=seat_price, secret_key=sk,
                                    userId=None, airline_order=order_id, state=False)
        o_info.save()
        return JsonResponse({"payment_provider": "WS", "secret_key": o_info.secret_key})

def Payment_Order(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        key_flag = req.get("uid") and req.get("Airline_order") and len(req) == 2
        if key_flag:
            uid = req["uid"]
            Air_line = req["Airline_order"]
        c_order = payRecord.objects.get(airline_order=Air_line)
        u = User.objects.get(id=uid)
        if u.deposit >= c_order.money:
            c_order.userId = u
            c_order.save()
            u.save()
            return JsonResponse({"msg": c_order.secret_key})
        else:
            return JsonResponse({"msg": "No enough money!"})

def Payment_Check(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        key_flag = req.get("state") and req.get("order_id") and len(req) == 2
        if key_flag:
            state = req["state"]
            Aie_line = req["order_id"]
        if state == "successful":
            c_order = payRecord.objects.get(airline_order=Aie_line)
            c_order.state = state
            c_order.save()
            u = User.objects.get(id=c_order.userId.id)
            u.deposit = u.deposit - c_order.money
            u.save()
            return JsonResponse({"state": "paid"})
        else:
            return JsonResponse({"state": "unpaid"})

def Payment_Return(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        key_flag = req.get("state") and req.get("order_id") and len(req) == 2
        if key_flag:
            state = req["state"]
            Aie_line = req["order_id"]
        if state == "successful":
            c_order = payRecord.objects.get(airline_order=Aie_line)
            c_order.state = False
            c_order.save()
            time = datetime.now()
            sk = secrets.token_hex(8)
            u = User.objects.get(id=c_order.userId.id)
            u.deposit = float(u.deposit) + float(c_order.money)
            u.save()
            c_order1 = payRecord(time=time, recipient="income", amount=1, money=c_order.Money,
                                          secret_key=sk, userId=u, airline_order=0, state=True)
            c_order1.save()
            return JsonResponse({"state": "canceled"})
        else:
            return JsonResponse({"state": "uncanceled"})