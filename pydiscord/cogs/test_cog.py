from discord.ext.commands import Cog, Bot, command, Context


class ExampleCog(Cog):
    def __init__(self, bot: Bot):
        self._bot: Bot = bot

    @command()
    async def hello(self, ctx: Context):
        await ctx.send("Hello from Cog!")
