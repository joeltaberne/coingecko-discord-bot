import os
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

if not TOKEN:
    print("Discord token is not set, please set it in your .env file")
else:
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)