import sys
sys.path.append('Classes')

import discord
from MessageHandler import MessageHandler
from decouple import config


class myClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.messageHandler = MessageHandler()

    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))


    async def on_message(self, message):
        if message.author == self.user:
            return

        returnMessage = self.messageHandler.getReturnMessage(message)

        if not returnMessage:
            return

        await message.channel.send(returnMessage)


client = myClient()
client.run(config('DISCORDSECRET'))



