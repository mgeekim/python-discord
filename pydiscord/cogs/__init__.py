from typing import List

from discord.ext.commands import Bot, Cog

from pydiscord.cogs.test_cog import ExampleCog


def get_all_cogs(bot: Bot) -> List[Cog]:
    return [
        ExampleCog(bot)
    ]
