# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# DJANGO auth tutorial on UDEMY by John Elder : https://www.udemy.com/build-a-user-authentication-web-app-with-python-and-django/

def login_user(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')
            else:
                messages.success(request, ('Error logging in - Please try again ..'))
                return redirect('/login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You have sucessfully logged out"))
    return redirect('/')

def register_user(request):
    return render(request, 'register.html')


def home_page(request):
    import requests
    import json

    #crypto prices for ticker at top
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,TRX&tsyms=USD")
    price = json.loads(price_request.content)


    pricesNdInfo_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,LTC,BCH,EOS,XLM,XMR,ADA,TRX&tsyms=USD")
    prices = json.loads(pricesNdInfo_request.content)

    return render(request, 'home.html', {'price':price, 'prices':prices})


# News page rendering and pulling API of NEWS and PRICES learned from UDEMY class by John Elder:
# https://www.udemy.com/build-a-crypto-currency-news-site-with-python-and-django/learn/v4/overview
def news_page(request):
    import requests
    import json
    # crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'news.html', {'api': api})




def portfolio_page(request):
    import requests
    import json

    #get prices and info
    #
    pricesPortfolio_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,LTC,BCH,EOS,XLM,XMR,ADA,TRX&tsyms=USD,BTC")
    pricesP = json.loads(pricesPortfolio_request.content)
    return render(request, 'portfolio.html', {'prices':pricesP})
