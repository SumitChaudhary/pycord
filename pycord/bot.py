import os
import discord
import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)

#print('Token is ___{0}____'.format(TOKEN))

@client.event
async def on_ready():
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
    print(
        f'{bot.user.name} with id {bot.user.id} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$time?'):
        await message.channel.send('Time now at greenwich meridian is : {0}'.format(datetime.datetime.now()))

    if message.content == "cookie":
        await message.channel.send(":cookie:")

client.run(TOKEN)