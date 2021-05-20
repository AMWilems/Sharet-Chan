import discord
import os
import chat_response
import console_text
#imports commands for discord lib
from discord.ext import commands

#imports dotenv for masking private data from git and unwanted users
from dotenv import load_dotenv

load_dotenv("/home/pi/Documents/Sharet-Chan/.gitignore/.env") #TODO convert to relative at some point. will have to be changed if moved

client = discord.Client()

TOKEN = os.getenv("TOKEN") 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('initial login ', console_text.get_time())

#listens for action within server to
#determine which action group function to call

#REFACTOR 05/20/21 04:25 LEXXLESS
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send(chat_response.check_contents(message))

client.run(TOKEN)

#using https://docs.python.org/3.5/library/os.html#os.environ to figure out dotenv
#using 
