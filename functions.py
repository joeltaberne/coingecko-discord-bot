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
                return(check_price(msg_a[2],msg_a[3]))
            else:
                return("Wrong format!\nTry !cg price coin1 coin2")
        elif msg_a[1] == "setalert":
            print('u selected setalert')

def check_price(m1,m2):
    url = api_url+"/coins/{}".format(m1)
    r = requests.get(url)
    if r:
        price = r.json()['market_data']['current_price'][m2]
        msg = "1 {}".format(m1)+" = {}".format(price)+" {}".format(m2)
        return(msg)
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
                        price = r.json()['market_data']['current_price'][m2]
                        msg = "1 {}".format(m1)+" = {}".format(price)+" {}".format(m2)
                        return(msg)


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