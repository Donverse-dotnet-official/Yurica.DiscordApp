from typing import Union
from discord import Client, RawAppCommandPermissionsUpdateEvent, Interaction
from discord.app_commands import Command, ContextMenu

class ApplicationCommandEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_raw_app_command_permissions_update(payload: RawAppCommandPermissionsUpdateEvent):
            pass

        @self.bot.event
        async def on_app_command_completion(interaction: Interaction, command: Union[Command, ContextMenu]):
            pass
