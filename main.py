import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import core
from core.ai_excuses import make_excuse
from core.chat import ai_chat

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

@bot.tree.command(name="tanya", description="Ask the bot anything")
@app_commands.describe(pertanyaan="What do you want to ask?")
async def tanya(interaction: discord.Interaction, pertanyaan: str):
    await interaction.response.defer()
    answer = await ai_chat(pertanyaan)
    quoted = pertanyaan.replace("\n", " ")[:300]
    await interaction.followup.send(
        f"{interaction.user.display_name} asked:\n> {quoted}\n\n{answer}",
        allowed_mentions=discord.AllowedMentions.none(),
    )
bot.run(TOKEN)