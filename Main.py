import discord
import os
import chat_repsonse

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
    print("initial login

@client.event
#listens for action within server to
#determine which action group function to call

#REFACTOR 05/20/21 04:25 LEXXLESS

async def on_message(message):                              #TODO possibly change to switch statement for readabilty
    if message.author == client.user:
        return
    
    if message.content.startswith('$'):
        chat_response.check_contents():
            
    if message.contents.startswith('!'):
        return                                              #TODO add in other actions here (such as music call in)
    
##  if message.content.startswith('$hey Sharet-Chan'):
##    await message.channel.send('Hello! UwU')              #TODO remove after testing chat_response file

client.run(TOKEN)

#using https://docs.python.org/3.5/library/os.html#os.environ to figure out dotenv
#using 
