from discord import Client, Entitlement

class EntitlementEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_entitlement_create(entitlement: Entitlement):
            print(f'SKU stored: {entitlement.user_id} in {entitlement.guild_id}')

        @self.bot.event
        async def on_entitlement_update(entitlement: Entitlement):
            print(f'SKU updated: {entitlement.user_id} in {entitlement.guild_id}')

        @self.bot.event
        async def on_entitlement_delete(entitlement: Entitlement):
            print(f'SKU deleted: {entitlement.user_id} in {entitlement.guild_id}')
