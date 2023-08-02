
import requests
from typing import Final
from dataclasses import dataclass

BASE_URL:Final[str] ="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

@dataclass
class Coin:
    name:str
    symbol:str
    current_price:float
    high_24h:float
    low_24h:float
    price_change:float
    price_change_percentage:float

    def __str__(self):
        return f'{self.name} ({self.symbol}): ${self.current_price :,}'
    

def get_coin()->list[Coin]:
    payload:dict = {'vs_currency':'usd','order':'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json:dict = data.json()

    coin_list:list[Coin]=[]
    for item in json:
        current_coin:Coin=Coin(
            name= item.get('name'),
            symbol= item.get('symbol'),
            current_price= item.get('current_price'),
            high_24h= item.get('high_24h'),
            low_24h= item.get('low_24h'),
            price_change = item.get('price_change_24h'),
            price_change_percentage= item.get('price_change_percentage')
        )
        coin_list.append(current_coin)
    
    return coin_list


# if __name__=='__main__':
#     coins= get_coin()
#     for coin in coins:
#         print(coin)
#^^ that prints all the cryptos



# ---------------main func-------------------


def alert(symbol:str, bottom:float, top:float, coins_list:list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price<bottom:
                print(coin,'TRIGGERED!!')
            else:
                print(coin)

if __name__ =="__main__":
    coins:list[Coin]= get_coin()

    # while True:
        # time.sleep(5)
    alert('btc', bottom=22_000,top=28_000, coins_list=coins )
    alert('etc', bottom=10_000,top=28_000, coins_list=coins )
    alert('xrp', bottom=0.54,top=2, coins_list=coins )
    alert('ada', bottom=0.50,top=4, coins_list=coins )


