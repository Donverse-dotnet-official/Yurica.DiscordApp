from discord import Client, Role


class RoleEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_guild_role_create(role: Role):
            pass

        @self.bot.event
        async def on_guild_role_delete(role: Role):
            pass

        @self.bot.event
        async def on_guild_role_update(before: Role, after: Role):
            pass
