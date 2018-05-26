print ("hello,world")
import requests
from bs4 import BeautifulSoup

print("Hello world")

target_url = 'https://bitflyer.jp/?bf=hhbmzc42'

r = requests.get(target_url)

soup = BeautifulSoup(r.text, "html.parser")
vals = soup.select_one("#bfPriceAsk_1").findAll(text=True)
buy_price=''.join(vals)
buy_price = soup.select_one("#bfPriceAsk_1").string

print(buy_price)
