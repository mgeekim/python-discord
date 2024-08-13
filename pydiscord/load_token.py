import os

from dotenv import load_dotenv


def load_token() -> str:
    load_dotenv()
    return os.getenv('DISCORD_TOKEN')
