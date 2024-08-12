from discord import Client, Guild, Integration, RawIntegrationDeleteEvent
from discord.abc import GuildChannel


class IntegrationEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_integration_create(integration: Integration):
            print(f'Created integration: {integration.guild.id}')

        @self.bot.event
        async def on_integration_update(integration: Integration):
            print(f'Updated integration: {integration.guild.id}')

        @self.bot.event
        async def on_guild_integrations_update(guild: Guild):
            print(f'Guild integration action: {guild.id}')

        @self.bot.event
        async def on_webhooks_update(channel: GuildChannel):
            print(f'Webhook updated: {channel.guild.id}')

        @self.bot.event
        async def on_raw_integration_delete(payload: RawIntegrationDeleteEvent):
            print(f'Integration deleted: {payload.integration_id}')
