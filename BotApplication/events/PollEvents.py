from discord import Client, RawPollVoteActionEvent


class PollEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_raw_poll_vote_add(payload: RawPollVoteActionEvent):
            pass

        @self.bot.event
        async def on_raw_poll_vote_remove(payload: RawPollVoteActionEvent):
            pass
