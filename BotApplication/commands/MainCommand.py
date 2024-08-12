from discord import Client, Interaction
from discord.app_commands import Choice, Group, command, describe, autocomplete


class MainCommands(Group):
    def __init__(self, bot: Client):
        super().__init__(
            name="yurica-ctl",
            description="Yurica's commands."
        )
        self.bot = bot

    @command(
        name="help",
        description="Get help."
    )
    async def help(self, interaction: Interaction):
        await interaction.response.defer()

        # Get server command prefix and get the help message from the database

        prefix = "$yurica"
        message = f"**{prefix} help** - Get help.\n"

        await interaction.followup.send(
            content=message,
            ephemeral=True
        )
