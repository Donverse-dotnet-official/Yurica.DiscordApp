import os
from dotenv import load_dotenv

from DiscordClient import DiscordClient

# Load the environment variables
load_dotenv('./env/.env')

# Create and start the Discord client
client = DiscordClient(
    token=os.getenv('DISCORD_TOKEN'),
    shard_id=os.getenv('DISCORD_SHARD_ID'),
    shard_total=os.getenv('DISCORD_SHARD_TOTAL')
).start()
