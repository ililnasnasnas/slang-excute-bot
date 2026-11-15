import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from core.excuses import make_excuse

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = Bot()

@bot.event
async def on_ready():
    print(f"Online as {bot.user}")

@bot.tree.command(name="alasan", description="Bikin alasan telat versi slang")
@app_commands.describe(chaos="Level chaos 0-2")
async def alasan(interaction: discord.Interaction, chaos: app_commands.Range[int, 0, 2] = 1):
    await interaction.response.send_message(make_excuse(interaction.user.id, chaos))

bot.run(TOKEN)