import discord
import os

client = discord.Client()
#TOKEN  = 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hey Sharet-Chan'):
        await message.channel.send('Hello! OWO')

client.run('ODQxNzk5OTY4OTgwMzM2Njcx.YJsBUA.1_0jkgNT0uwpaeCU4s0aJZ6uj8U')
