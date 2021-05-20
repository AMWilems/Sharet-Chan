import discord
import os
import console_text

from discord.ext import commands

client = discord.Client()

def check_contents(message):                              #TODO possibly change to switch statement for readabilty  
    if message.content.startswith('$'):
       reply = check_verbage(message)
       return reply
       
    if message.content.startswith('!'):
        return

def check_verbage(message):
    if message.content.__contains__('hey'):
        text = "Hi everybody! ＼(^o^)／"
        print(console_text.get_time(), "Said hi to everyone in",
              message.guild.name,':', message.channel.name)
    return text