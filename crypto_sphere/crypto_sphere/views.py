from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    import requests
    import json

    #crypto prices
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,TRON&tsyms=USD")
    price = json.loads(price_request.content)


    # crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price':price})
