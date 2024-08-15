import discord
from discord.ext import commands
from discord.ext.commands import Bot

from pydiscord.cogs import get_all_cogs
from pydiscord.env_man import EnvManager


class PyDiscord:
    def __init__(self):
        self._intents = discord.Intents.default()
        self._intents.message_content = True
        self._env_manager = EnvManager()

    def start(self):
        bot: Bot = commands.Bot(
            command_prefix='!',
            intents=self._intents
        )

        @bot.event
        async def on_ready():
            print(f'Logged in as {bot.user}')
            for b in get_all_cogs(bot):
                await bot.add_cog(b)

        bot.run(self._env_manager.load_token())
