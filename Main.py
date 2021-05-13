import discord
import os

from discord.ext import commands

from dotenv import load_dotenv

from pathlib import Path

dotenv_path = Path("/home/pi/Documents/Sharet-Chan/.gitignore/.env")

load_dotenv(dotenv_path=dotenv_path)

client = discord.Client()

TOKEN = os.getenv("TOKEN") #currently returns as null, causes us not to be able to run code

#TOKEN='ODQxNzk5OTY4OTgwMzM2Njcx.YJsBUA.sOhB0fxeWjyPSGsToe8iz3JqHmE'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hey Sharet-Chan'):
        await message.channel.send('Hello! UwU')

client.run(TOKEN)

#using https://docs.python.org/3.5/library/os.html#os.environ to figure out dotenv
#using 
