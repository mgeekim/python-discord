import os

from dotenv import load_dotenv


class EnvManager:
    def __init__(self):
        load_dotenv()

    def load_token(self) -> str:
        return os.getenv('DISCORD_TOKEN')

    def get_channel_id(self) -> int:
        return int(os.getenv('CHANNEL_ID'))
