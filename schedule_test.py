import schedule, time, requests
def hello_world():
    print(f'Hello World {time.ctime()}')
def backend_16_1b():
    print(f'Здравствуйте, сегодня у вас урок в 19:00')

# schedule.every(2).seconds.do(hello_world)
# schedule.every(1).minutes.do(hello_world)
# schedule.every().day.at("19:47").do(hello_world)
# schedule.every().monday.at("19:49").do(hello_world)
# schedule.every().day.at("19:52", "Asia/Bishkek").do(hello_world)
# schedule.every().monday.at("19:56").do(backend_16_1b)

def get_btc_price():
    responce = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    data = responce.json()
    price = data['price']
    print(f'Цена биткоина на {time.ctime()} составляет {price}')
schedule.every(1).second.do(get_btc_price)  

def get_eth_price():
    responce = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
    data2 = responce.json()
    price2 = data2['price']
    print(f'Цена эфириума на {time.ctime()} составляет {price2}')
schedule.every(1).second.do(get_eth_price)  

while True:
    schedule.run_pending()
    time.sleep(1)