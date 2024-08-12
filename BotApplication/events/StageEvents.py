from discord import Client, StageInstance


class StageEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_stage_instance_create(stage_instance: StageInstance):
            pass

        @self.bot.event
        async def on_stage_instance_delete(stage_instance: StageInstance):
            pass

        @self.bot.event
        async def on_stage_instance_update(before: StageInstance, after: StageInstance):
            pass
