from typing import List

from discord.ext.commands import Bot, Cog

from pydiscord.cogs.test_cog import ExampleCog
from pydiscord.cogs.yf_cog import YFCog


def get_all_cogs(bot: Bot) -> List[Cog]:
    return [
        ExampleCog(bot),
    ]
