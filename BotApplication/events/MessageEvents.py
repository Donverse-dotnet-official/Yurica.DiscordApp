from typing import List
from discord import Client, Message, RawBulkMessageDeleteEvent, RawMessageDeleteEvent, RawMessageUpdateEvent


class MessageEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_message(message: Message):
            if (message.author == self.bot.user):
                return

            print('Message received')

        @self.bot.event
        async def on_raw_message_edit(payload: RawMessageUpdateEvent):
            pass

        @self.bot.event
        async def on_raw_message_delete(payload: RawMessageDeleteEvent):
            pass

        @self.bot.event
        async def on_bulk_message_delete(payload: RawBulkMessageDeleteEvent):
            pass
