import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix = '$')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('BEEPBIPBIPEBEBBPEIBEIRIANWRIPONWA')



client.run(config('DISCORDSECRET'))



