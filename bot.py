import os

from functions import main
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("Discord token is not set, please set it in your .env file")
else:
    main(TOKEN)