from typing import Union
from discord import Client, Guild, Member, RawMemberRemoveEvent, User


class MemberEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_member_join(member: Member):
            pass

        # @self.bot.event
        # async def on_member_remove(member: Member):
        #     pass

        @self.bot.event
        async def on_raw_member_remove(payload: RawMemberRemoveEvent):
            pass

        @self.bot.event
        async def on_member_update(before: Member, after: Member):
            pass

        @self.bot.event
        async def on_user_update(before: User, after: User):
            pass

        @self.bot.event
        async def on_member_ban(guild: Guild, user: Union[User, Member]):
            pass

        @self.bot.event
        async def on_member_unban(guild: Guild, user: User):
            pass

        @self.bot.event
        async def on_presence_update(before: Member, after: Member):
            pass
