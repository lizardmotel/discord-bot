import discord
from discord.ext import commands
from decouple import config


class myClient(discord.Client):

    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))


    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('BEEPBIPBIPEBEBBPEIBEIRIANWRIPONWA')


client = myClient()

client.run(config('DISCORDSECRET'))



