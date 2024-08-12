from discord import Client, RawThreadDeleteEvent, RawThreadMembersUpdate, RawThreadUpdateEvent, Thread, ThreadMember


class ThreadEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_thread_create(thread: Thread):
            pass

        @self.bot.event
        async def on_thread_join(thread: Thread):
            pass

        @self.bot.event
        async def on_thread_remove(thread: Thread):
            pass

        @self.bot.event
        async def on_raw_thread_update(payload: RawThreadUpdateEvent):
            pass

        @self.bot.event
        async def on_raw_thread_delete(payload: RawThreadDeleteEvent):
            pass

        @self.bot.event
        async def on_thread_member_join(member: ThreadMember):
            pass

        @self.bot.event
        async def on_raw_thread_member_remove(payload: RawThreadMembersUpdate):
            pass
