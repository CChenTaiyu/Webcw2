import requests
import json


# api.1
def signin():
    url = "http://127.0.0.1:8000/PaymentWS/signin/"

    payload = {"username": "test", "password": "123456"}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def signup():
    url = "http://127.0.0.1:8000/PaymentWS/signup/"

    payload = {"username": "test", "password": "123456", "name": "test"}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def deposit():
    url = "http://127.0.0.1:8000/PaymentWS/deposit/"

    payload = {"uid": 6}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def information():
    url = "http://127.0.0.1:8000/PaymentWS/Payment Information/"
    payload = {"order_id": 200, "seat_price": 20, "airline_name": "airline_xyf"}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def statement():
    url = "http://127.0.0.1:8000/PaymentWS/statement/"

    payload = {"uid": 5}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def order():
    url = "http://127.0.0.1:8000/PaymentWS/Payment Order/"

    payload = {"uid": 5, "Airline_order": 200}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def check():
    url = "http://127.0.0.1:8000/PaymentWS/Payment Check/"

    payload = {"state": "True", "order_id": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def retu1n():
    url = "http://127.0.0.1:8000/PaymentWS/Payment Return/"

    payload = {"state": "False", "Airline_order": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def transfer():
    url = "http://127.0.0.1:8000/PaymentWS/transfer/"

    payload = {"uid": 5, "password": "123456", "u2": "cty", "u3": "cty", "money":1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def balance():
    url = "http://127.0.0.1:8000/PaymentWS/balance/"

    payload = {"uid": 5}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


if __name__ == '__main__':
    signup()
    signin()
    deposit()
    transfer()
    balance()
    statement()
    information()
    order()
    check()
    retu1n()
