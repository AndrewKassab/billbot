from discord.ext import commands
import cogs
import discord
from settings import DISCORD_TOKEN, logging


class BillBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!",intents=discord.Intents.default())

    async def setup_hook(self) -> None:
        await self.add_cog(cogs.Calculate(self))

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'We have logged in as {bot.user}')


bot = BillBot()
bot.run(DISCORD_TOKEN)
