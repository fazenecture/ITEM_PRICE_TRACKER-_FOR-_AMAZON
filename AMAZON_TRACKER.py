import requests
from bs4 import BeautifulSoup
import re
from discord_webhooks import DiscordWebhooks
import html5lib
import time

hook_url = 'YOU DISCORD WEBHOOOK URL'
webhook = DiscordWebhooks(hook_url)
headers = {"YOUR USER AGENT: to get this just search on google "My User agent" and copy paste it }


url = input("Enter Your Amazon Product Link : ")
d_price = input("Enter your desired price : ")
d_price = int(d_price)

while True:
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html5lib')
        title = soup.find(id="productTitle")
        print(title)
        title = title.get_text()
        title = title.strip()
        print(title)
        price = soup.find(id="priceblock_ourprice")
        print(price)

        price = price.get_text()
        con_price = price[2:]
        print(con_price, len(con_price), type(con_price))
        con_price_s = con_price.replace(',', '')
        dec = float(con_price_s)
        print(dec, type(dec))
        Dec = int(dec)
        print(dec)
        while True:
            if Dec < d_price:
                print("Price Decreased")
                decs = str(dec)
                webhook.set_content(content="Price of Decreased to Rs " + decs, title=title)
                webhook.send()
                break
            else:
                print("Same price")
                time.sleep(3)
                continue

    except:
        print("retrying...")
    else:
        break
