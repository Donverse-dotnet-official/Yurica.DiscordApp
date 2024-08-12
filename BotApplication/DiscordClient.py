from discord import Client, Intents
from discord.app_commands import CommandTree

from commands.MainCommand import MainCommands
from events.ApplicationCommandEvents import ApplicationCommandEvents
from events.AutoModEvents import AutoModEvents
from events.ChannelEvents import ChannelEvents, GuildChannelEvents, DMChannelEvents
from events.GatewayEvents import GatewayEvents
from events.GuildEvents import GuildEvents
from events.IntegrationEvents import IntegrationEvents
from events.InteractionEvents import InteractionEvents
from events.MemberEvents import MemberEvents
from events.MessageEvents import MessageEvents
from events.PollEvents import PollEvents
from events.ReactionEvents import ReactionEvents
from events.RoleEvents import RoleEvents
from events.ScheduledEventEvents import ScheduledEventEvents
from events.StageEvents import StageEvents
from events.ThreadEvents import ThreadEvents
from events.VoiceEvents import VoiceEvents


class DiscordClient:
    """
    Discord client for the bot

    Parameters
    ----------
    :param token: The Discord bot token
    :type token: str
    :param shard_id: The shard ID for the bot
    :type shard_id: int | str
    :param shard_total: The total number of shards for the bot
    :type shard_total: int | str
    """
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
        self.command_tree = CommandTree(self.bot)

        # Register event handlers
        self.application_command_events = ApplicationCommandEvents(self.bot)
        self.automod_events = AutoModEvents(self.bot)
        self.channel_events = ChannelEvents(self.bot)
        self.guild_channel_events = GuildChannelEvents(self.bot)
        self.dm_channel_events = DMChannelEvents(self.bot)
        self.gateway_events = GatewayEvents(self.bot, self.command_tree)
        self.guild_events = GuildEvents(self.bot)
        self.integration_events = IntegrationEvents(self.bot)
        self.interaction_events = InteractionEvents(self.bot)
        self.member_events = MemberEvents(self.bot)
        self.message_events = MessageEvents(self.bot)
        self.poll_events = PollEvents(self.bot)
        self.reaction_events = ReactionEvents(self.bot)
        self.role_events = RoleEvents(self.bot)
        self.scheduled_event_events = ScheduledEventEvents(self.bot)
        self.stage_events = StageEvents(self.bot)
        self.thread_events = ThreadEvents(self.bot)
        self.voice_events = VoiceEvents(self.bot)

        # Register application commands
        self.yurica_ctl = MainCommands(self.bot)

        # Append application commands to the command tree
        # self.command_tree.add_command(self.yurica_ctl)

    def start(self):
        """
        Start the Discord client
        """
        self.bot.run(self.token)

    async def stop(self):
        """
        Stop the Discord client
        """
        await self.bot.close()
