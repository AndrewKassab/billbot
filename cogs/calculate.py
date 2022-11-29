from discord.ext import commands
import discord
from settings import CALCULATE_COMMAND


class Calculate(commands.cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name=CALCULATE_COMMAND,
        description="Split and calculate a bill"
    )
    async def calculate_bill(self, interaction: discord.Interaction, participants: [str]):
        pass

    async def prompt_for_participants(self):
        pass

    async def add_item(self):
        pass

    async def print_results(self):
        pass
