from discord import Client, Member, VoiceState


class VoiceEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_voice_state_update(member: Member, before: VoiceState, after: VoiceState):
            if after.channel is not None:
                print(f'Voice state updated: {after.channel.id} in {after.channel.guild.id} with {member.id}')
            else:
                print(f'User {member.id} has disconnected from voice channel in {before.channel.id} on {before.channel.guild.id}')
