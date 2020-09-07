import os
from dotenv import load_dotenv
import datetime

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')
    
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'Server region is : {guild.region}')
    text_channels = '\n - '.join([channel.name for channel in guild.text_channels])
    print(f'Guild Text Channels:\n - {text_channels}')
    voice_channels = '\n - '.join([channel.name for channel in guild.voice_channels])
    print(f'Guild Voice Channels:\n - {voice_channels}')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'hello':
        await message.channel.send('howdy!')
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$time?'):
        await message.channel.send('Time now at greenwich meridian is : {0}'.format(datetime.datetime.now()))

    if message.content == "cookie":
        await message.channel.send(":cookie:")
    
    #add the following line else the bot stops processing after parsing the message. 
    await client.process_commands(message)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    

@client.event
async def on_member_remove(member):
    print(f'{member} has joined the server.')
    


@client.command()
async def ping(ctx):
    print(f'ping command detected')
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def test(ctx, *args):
    print(f'test command detected')
    await ctx.send('Command sent by {} with {} arguments: {}'.format(ctx.author, len(args), ', '.join(args)))

@client.command()
async def pic(ctx):
    print(f'pic command detected')        
    await ctx.send('https://images.freeimages.com/images/large-previews/389/mitze-1380778.jpg')

#Start the bot
client.run(TOKEN)