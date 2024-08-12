from discord import Client


class ConnectionEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_connect():
            print(f'Connected: {self.bot.user.id}')

        @self.bot.event
        async def on_disconnect():
            print(f'Disconnected: {self.bot.user.id}')

        @self.bot.event
        async def on_shard_connect(shard_id: int):
            print(f'Shard connected: {shard_id} / {self.bot.shard_count}')

        @self.bot.event
        async def on_shard_disconnect(shard_id: int):
            print(f'Shard disconnected: {shard_id} / {self.bot.shard_count}')
