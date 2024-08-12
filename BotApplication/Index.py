# TODO: Add commands to the command tree

import os
import threading
from dotenv import load_dotenv
from flask import Flask, request

from DiscordClient import DiscordClient


# Load the environment variables
load_dotenv('./.env/.env')

# Create and start the Discord client
client = DiscordClient(
    token=os.getenv('DISCORD_TOKEN'),
    shard_id=os.getenv('DISCORD_SHARD_ID'),
    shard_total=os.getenv('DISCORD_SHARD_TOTAL')
).start()
# Create the API
api = Flask(__name__)

@api.route('/shutdown')
async def stop_bot():
    client.stop()
    return 'Bot stopped'

# Run application
# if __name__ == '__main__':
#     bot_thread = threading.Thread(target=client.start)
#     api_thread = threading.Thread(target=api.run, kwargs={'port': 5000})
#     bot_thread.start()
    # api_thread.start()

    # runnable = True

    # while runnable:
    #     if not bot_thread.is_alive():
    #         runnable = False
    #     if not api_thread.is_alive():
    #         runnable = False
    # print('Application stopped')
