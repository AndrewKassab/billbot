from dotenv import load_dotenv
import os
import logging

load_dotenv()


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s;%(levelname)s;%(message)s")

# Environment Variables
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

# Slash Command names

# Emojis

