from discord import Client, ScheduledEvent, User


class ScheduledEventEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_scheduled_event_create(event: ScheduledEvent):
            pass

        @self.bot.event
        async def on_scheduled_event_delete(event: ScheduledEvent):
            pass

        @self.bot.event
        async def on_scheduled_event_update(before: ScheduledEvent, after: ScheduledEvent):
            pass

        @self.bot.event
        async def on_scheduled_event_user_add(event: ScheduledEvent, user: User):
            pass

        @self.bot.event
        async def on_scheduled_event_user_remove(event: ScheduledEvent, user: User):
            pass
