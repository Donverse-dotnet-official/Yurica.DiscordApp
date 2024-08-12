from datetime import datetime
from typing import Union, Optional
from discord import Client, Thread, GroupChannel, RawTypingEvent
from discord.abc import GuildChannel, PrivateChannel


class ChannelEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_raw_typing(payload: RawTypingEvent):
            pass

class GuildChannelEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_guild_channel_create(channel: GuildChannel):
            print(f'Channel created: {channel.id}')

        @self.bot.event
        async def on_guild_channel_delete(channel: GuildChannel):
            print(f'Channel deleted: {channel.id}')

        @self.bot.event
        async def on_guild_channel_update(before: GuildChannel, after: GuildChannel):
            print(f'Channel updated: {after.id}')

        @self.bot.event
        async def on_guild_channel_pins_update(channel: Union[GuildChannel, Thread], last_pin: Optional[datetime]):
            print(f'Message pinned: {channel.id}')

class DMChannelEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_private_channel_update(before: GroupChannel, after: GroupChannel):
            print(f'DMChannel updated: {after.id}')

        @self.bot.event
        async def on_private_channel_pins_update(channel: PrivateChannel, last_pin: Optional[datetime]):
            print(f'Message pinned: {channel.id}')
