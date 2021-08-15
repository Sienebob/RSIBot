import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

client = Client(config.API_KEY, config.API_SECRET) #removed , tld='us'

