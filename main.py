#!/usr/bin/env python3
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Create an Intents object with all intents enabled
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
#dowload env
load_dotenv(dotenv_path="config")
class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

        async def on_ready(self):
            print(f"{self.user.display_name} est connecte au serveur.")
            doc_bot = DocBot()

# Create the Discord client with intents
client  = discord.Client(intents=intents)

#on_ready to indicate the Bot is ready
@client.event
async def on_ready():
   print("Le Bot est prét.")
   doc_bot.run(os.getenv("TOKEN"))
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(1281667040024858716)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

#on_message to chat with the Bot
@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong")  


        # Run the bot with the token
client.run("")

