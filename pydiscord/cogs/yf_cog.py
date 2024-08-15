from discord.ext import tasks
from discord.ext.commands import Cog, Bot, command, Context

from pydiscord.yf.yf import YF


class YFCog(Cog):
    def __init__(self, bot: Bot, channel_id: int):
        self._bot: Bot = bot
        self._channel_id: int = channel_id
        self._yf = YF()

        self.send_message.start()

    def cog_unload(self):
        self.send_message.cancel()

    @command()
    async def change_ticker(self, ctx: Context, ticker: str):
        self._yf.set_ticker(ticker)
        await ctx.send(f"Set ticker {ticker}!")

    @tasks.loop(minutes=1)
    async def send_message(self):
        channel = self._bot.get_channel(self._channel_id)
        for news in self._yf.monitor_news():
            if channel is not None:
                await channel.send(news.link)

    @send_message.before_loop
    async def before_send_message(self):
        print('Waiting until bot is ready...')
        await self._bot.wait_until_ready()
