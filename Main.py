import discord
import os
#imports commands for discord lib
from discord.ext import commands
#imports dotenv for masking private data from git and unwanted users
from dotenv import load_dotenv
#may not keep used to help gather path for .env file 
#from pathlib import Path

#dotenv_path = Path(str('/.env'))

load_dotenv("/home/pi/Documents/Sharet-Chan/.gitignore/.env") #TODO convert to relative at some point. will have to be changed if moved

client = discord.Client()

TOKEN = os.getenv("TOKEN") 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
#listens for action within server to messagge user back with simple hello statement 
async def on_message(message): #TODO remove and move to command file once path to gitignore is figured out
    if message.author == client.user:
        return

    if message.content.startswith('$hey Sharet-Chan'):
        await message.channel.send('Hello! UwU')

client.run(TOKEN)

#using https://docs.python.org/3.5/library/os.html#os.environ to figure out dotenv
#using 
