import json
import requests
from django.shortcuts import render


def home(request):
    # Grab price data
    price_request = \
        requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,'
                     'MIOTA,TRX&tsyms=USD,EUR,BRL')
    price = json.loads(price_request.content)

    # Grab article data
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    
    return render(request, 'currency/home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        quote_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+
                                     '&tsyms=USD,EUR,BRL')
        crypto = json.loads(quote_request.content)
        return render(request, 'currency/prices.html', {'crypto': crypto})
    else:
        notfound = 'Type the crypto symbol into the box above...'
        return render(request, 'currency/prices.html', {'notfound': notfound})
