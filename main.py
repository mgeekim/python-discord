import discord
from discord.ext import commands
from discord.ext.commands import Bot

from pydiscord.cogs import get_all_cogs
from pydiscord.load_token import load_token

intents = discord.Intents.default()
intents.message_content = True

bot: Bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    for b in get_all_cogs(bot):
        await bot.add_cog(b)


bot.run(load_token())
