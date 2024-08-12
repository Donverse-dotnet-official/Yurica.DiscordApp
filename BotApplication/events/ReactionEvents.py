from discord import Client, RawReactionActionEvent, RawReactionClearEmojiEvent, RawReactionClearEvent


class ReactionEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_raw_reaction_add(payload: RawReactionActionEvent):
            pass

        @self.bot.event
        async def on_raw_reaction_remove(payload: RawReactionActionEvent):
            pass

        @self.bot.event
        async def on_raw_reaction_clear(payload: RawReactionClearEvent):
            pass

        @self.bot.event
        async def on_raw_reaction_clear_emoji(payload: RawReactionClearEmojiEvent):
            pass
