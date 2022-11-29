from dotenv import load_dotenv
import os
import mysql.connector
import sqlite3
import logging

load_dotenv()


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s;%(levelname)s;%(message)s")

# Database
db = sqlite3

# Environment Variables
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

# Slash Command names

# Emojis

