import discord
import os

client = discord.Client()
#TOKEN  = Removed for movement to rasberry PI via upload to GITHUB

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hey Sharet-Chan'):
        await message.channel.send('Hello! OWO')

client.run('TOKEN')
