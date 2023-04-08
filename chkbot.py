import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message.content)
client.run('token')
# await bot.process_commands(message)
