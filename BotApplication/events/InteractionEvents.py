from discord import Client, Interaction, InteractionType


class InteractionEvents:
    def __init__(self, bot: Client):
        self.bot = bot
        self.register()

    def register(self):
        @self.bot.event
        async def on_interaction(interaction: Interaction):

            if interaction.type == InteractionType.application_command:
                print(f'AppCommand fired: {interaction.id} in {interaction.guild_id}')
                # The implementation are must use discord.py annotations
                # Example:
                # @bot.tree.command(name='ping', description='Pong!')
                # async def ping(ctx):
                #     await ctx.send('Pong!')
            elif interaction.type == InteractionType.autocomplete:
                print(f'Autocomplete fired: {interaction.id} in {interaction.guild_id}')
                # The implementation are must use discord.py annotations
                # Example:
                # @bot.tree.command(name='ping', description='Pong!')
                # @discord.app_commands.autocomplete(greet=greet_autocomplete_function)
                # async def ping(ctx, greet: str):
                #     await ctx.send('Pong! ' + greet)
            elif interaction.type == InteractionType.component:
                print(f'Component fired: {interaction.id} in {interaction.guild_id}')
                # The implementation is use component handler
                # TODO: Add implementation for component handler
            elif interaction.type == InteractionType.modal_submit:
                print(f'Modal Submit fired: {interaction.id} in {interaction.guild_id}')
                # The implementation is use modal handler
                # TODO: Add implementation for modal handler
