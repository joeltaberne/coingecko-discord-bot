import os
import discord
import requests
import math

client = discord.Client()

api_url="https://api.coingecko.com/api/v3"

def parse_message(message_content):
    msg_a = message_content.split(' ')
    if msg_a[0] == "!cg":
        if msg_a[1] == "price":
            if len(msg_a) == 4:
                return(price_message(msg_a[2],msg_a[3]))
            else:
                return("Wrong format!\nTry !cg price coin1 coin2")
        elif msg_a[1] == "setalert":
            print('u selected setalert')
        # elif msg_a[1] == "list":
        #     return(list_message())

def get_price(m1,m2):
    url = api_url+"/coins/{}".format(m1)
    r = requests.get(url)
    if r:
        price = r.json()['market_data']['current_price'][m2]
        return(price)
    else:
        url = api_url+"/coins/list"
        r = requests.get(url)
        if r:
            for i in r.json():
                if i['symbol'] == m1:
                    m1 = i['id']
                    url = api_url+"/coins/{}".format(m1)
                    r = requests.get(url)
                    if r:
                        try:
                            print(r.json()['market_data']['current_price'][m2])
                            return(r.json()['market_data']['current_price'][m2])
                        except KeyError as e:
                            pass

def price_message(m1,m2):
    price = get_price(m1,m2)
    if price:
        if price >= 0:
            return("{}".format(m1.upper())+"/{}".format(m2.upper())+" - {}".format(price))
        else:
            return("Market not found, please try again.")
    else:
        return("Market not found, please try again.")

# def list_message():
#     url = api_url+"/coins/list"
#     r = requests.get(url)
#     message = "Available coins:\n"
#     if r:
#         for i in r.json():
#             message = message + i['name'] + ", "
#         return(message)

# def set_alert(m1,m2,price):
#     url = api_url+"/coins/{}".format(m1)
#     r = requests.get(url)
#     if r:
#         price = r

def main(TOKEN):
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        message_content = message.content
        response = parse_message(message_content)
        if response:
            await message.channel.send(response)

    client.run(TOKEN)