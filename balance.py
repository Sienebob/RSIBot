import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

client = Client(config.API_KEY, config.API_SECRET) #removed , tld='us'

#LIVE AND PERFORMING
   
try:
 #   order = client.order_market_buy(
    symbol='LTOUSDT',
    quantity=32)

except BinanceAPIException as e:
    # error handling goes here
    print(e)
except BinanceOrderException as e:
    # error handling goes here
    print(e)