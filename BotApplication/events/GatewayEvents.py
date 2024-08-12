from discord import Activity, ActivityType, Client, Status
from discord.app_commands import CommandTree


class GatewayEvents:
    def __init__(self, bot: Client, command_tree: CommandTree):
        self.bot = bot
        self.command_tree = command_tree
        self.register()


    def register(self):
        @self.bot.event
        async def on_ready():
            print(f'Client is ready {self.bot.user.name} ({self.bot.user.id})')
            try:
                synced = await self.command_tree.sync()
                if synced:
                    print(f'Synced command tree: with {len(synced)} commands')
            except Exception as e:
                print(f'Error while syncing command tree: {e}')

            await self.bot.change_presence(
                status=Status.idle,
                activity=Activity(
                    name=f'Shard {self.bot.shard_id} / {self.bot.shard_count} with {len(self.bot.guilds)} guilds',
                    type=ActivityType.watching
                )
            )

        @self.bot.event
        async def on_resumed():
            print(f'Client is resumed {self.bot.user.name} ({self.bot.user.id})')

        @self.bot.event
        async def on_shard_ready(shard_id):
            print(f'Shard is ready {shard_id} / {self.bot.shard_count}')

        @self.bot.event
        async def on_shard_resumed(shard_id):
            print(f'Shard is resumed {shard_id} / {self.bot.shard_count}')
