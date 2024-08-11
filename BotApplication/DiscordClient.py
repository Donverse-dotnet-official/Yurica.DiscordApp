from discord import Client, Intents
from discord.app_commands import CommandTree

class DiscordClient:
    def __init__(
        self,
        token: str,
        shard_id: int | str,
        shard_total: int | str
    ):
        # Connect to backend API services

        # Setup the bot
        self.token = token
        self.intents = Intents()
        self.intents.message_content = True
        self.intents.auto_moderation_configuration = True
        self.intents.auto_moderation_execution = True
        self.intents.messages = True
        self.intents.typing = True
        self.intents.guilds = True
        self.intents.emojis_and_stickers = True
        self.intents.moderation = True
        self.intents.integrations = True
        self.intents.webhooks = True
        self.intents.members = True
        self.intents.moderation = True
        self.intents.presences = True
        self.intents.reactions = True
        self.intents.guild_scheduled_events = True
        self.intents.voice_states = True

        # Create the bot
        self.bot = Client(
            intents=self.intents,
            shard_id=int(shard_id),
            shard_count=int(shard_total)
        )

        # Create the command tree for application commands
        self.bot.command_tree = CommandTree(self.bot)

        # Register event handlers

        # Register application commands

        # Append application commands to the command tree

    def start(self):
        self.bot.run(self.token)

    def stop(self):
        self.bot.close()
