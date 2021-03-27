import os
import discord

client = discord.Client()

def parse_message(message_content):
    print(message_content)

def main(TOKEN):
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        message_content = message.content
        parse_message(message_content)

    client.run(TOKEN)