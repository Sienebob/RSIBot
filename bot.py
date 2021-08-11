import websocket, json, pprint, talib, numpy

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
RSI_PERIOD = 4
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

TRADE_SYMBOL = 'ETHUSDT'
#TEADE_QUANTITY 0.005


closes = []

in_position = False

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('Closed connection')

def on_message(ws, message):
    global closes
    print('recieved message')
    json_message = json.loads(message)
    
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)
        
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsi:s calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print ("Overbought, SELL SELL SELL!")
                    #put binance sell logick here

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("Oversold, but you already own it, nothing to do.")
                else:
                    print ("Oversold, BUY BUY BUY!")
                    #put binance buy logick here

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

ws.run_forever()