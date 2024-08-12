from discord import Client, AutoModRule, AutoModAction

class AutoModEvents:
    def __init__(self, bot: Client,):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_automod_rule_create(rule: AutoModRule):
            print(f'Triggered!!')

        @self.bot.event
        async def on_automod_rule_update(rule: AutoModRule):
            print(f'Triggered!!')

        @self.bot.event
        async def on_automod_rule_delete(rule: AutoModRule):
            print(f'Triggered!!')

        @self.bot.event
        async def on_automod_action(execution: AutoModAction):
            print(f'Triggered!!')
