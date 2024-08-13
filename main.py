import discord
from discord.ext import commands

from pydiscord.cogs.test_cog import ExampleCog
from pydiscord.load_token import load_token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.add_cog(ExampleCog(bot))


bot.run(load_token())
