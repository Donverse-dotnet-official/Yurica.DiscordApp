from typing import Sequence
from discord import AuditLogEntry, Client, Emoji, Guild, GuildSticker, Intents, Invite

class GuildEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_guild_available(guild: Guild):
            print(f'Available guild: {guild.name}')

        @self.bot.event
        async def on_guild_unavailable(guild: Guild):
            print(f'Unavailable guild: {guild.name}')

        @self.bot.event
        async def on_guild_join(guild: Guild):
            print(f'Joined guild -> {guild.name}')

        @self.bot.event
        async def on_guild_remove(guild: Guild):
            print(f'Leaved guild from {guild.name}')

        @self.bot.event
        async def on_guild_update(before: Guild, after: Guild):
            print(f'Guild updated: {after.name}')

        @self.bot.event
        async def on_guild_emojis_update(guild: Guild, before: Sequence[Emoji], after: Sequence[Emoji]):
            print(f'Emojis updated: {guild.id}')

        @self.bot.event
        async def on_guild_stickers_update(guild: Guild, before: Sequence[GuildSticker], after: Sequence[GuildSticker]):
            print(f'Stickers updated: {guild.id}')

        @self.bot.event
        async def on_audit_log_entry_create(entry: AuditLogEntry):
            print(f'Audit recorded: {entry.guild.id}')

        @self.bot.event
        async def on_invite_create(invite: Invite):
            print(f'Invite created: {invite.guild.id}')

        @self.bot.event
        async def on_invite_delete(invite: Invite):
            print(f'Invite deleted: {invite.guild.id}')
