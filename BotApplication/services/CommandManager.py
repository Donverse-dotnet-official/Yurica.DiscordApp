from typing import Any
from discord import Guild
from discord.app_commands import CommandTree, Command, ContextMenu, Group

def register_guild_command(tree: CommandTree, guild: Guild, command: Command[Any, ..., Any] | ContextMenu | Group):
    """
    Register the guild commands for the bot

    Parameters
    ----------
    :param tree: The command tree for the bot
    :type tree: CommandTree
    :param guild: The guild to register the command for
    :type guild: Guild
    :param command: The command to register for the guild
    :type command: function
    """
    # Register the command for the guild
    tree.add_command(command, guild=guild)
