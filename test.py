import requests
import json


r = requests.post("http://localhost:5000/register/", json={"name": "login_name", "password": "password"})
print(r.text)

r = requests.post("http://localhost:5000/login/", json={"name": "login_name", "password": "password"})
print(r.text)
# r = requests.get("http://127.0.0.1:5000/")


# data = json.loads(r.text)

# rates = data.get("rates")

# list_n = list(rates.keys())

# print(list_n)
# print("--------")

# from_currency = input("Select from curency: ")
# to_currency = input("Select to currency: ")
# amount = int(input("Enter an amount: "))

# result = amount / rates.get(from_currency) * rates.get(to_currency)

# print(f"{amount} {from_currency} = {result} {to_currency}")