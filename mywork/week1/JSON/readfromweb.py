# Playing with JSON.
# program to read from the web
# PFDA - Topic 1 - getting started
# Author: Ermelinda Qejvani
# Based on lectures by Andrew Beatty

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])
