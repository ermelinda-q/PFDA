# Programming for Data Analytics
# Week 1 - Data representation.
# Lab 01 - read JSON from internet.
# Author: Ermelinda Qejvani

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()
# print(data)     # all JSON file
print(data['bpi']['EUR']['rate_float']) # just euro prices