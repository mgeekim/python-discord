from typing import List

from discord.ext.commands import Bot, Cog

from pydiscord.cogs.test_cog import ExampleCog
from pydiscord.cogs.yf_cog import YFCog
from pydiscord.env_man import EnvManager


def get_all_cogs(bot: Bot, env_man: EnvManager) -> List[Cog]:
    return [
        ExampleCog(bot),
        YFCog(bot, env_man.get_channel_id()),
    ]
