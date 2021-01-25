import discord
import random

class ImageHandler:
    def sendImage(self, messageList):
        result = self.getRandomMessage(messageList)

        return result

    def getRandomMessage(self, messageList):
        imageList = self.getFilteredList(messageList)

        if imageList == []:
            return 'No images found, get to snapping.'

        randomMessage = random.choice(imageList)

        return randomMessage

    def getFilteredList(self, messageList):
        uniqueFilenames = []
        imageMessages = []

        for msg in messageList:
            if (msg.author.bot
                    or msg.attachments == []
                    or msg.attachments[0].height == None
                    or uniqueFilenames.count(msg.attachments[0].filename) > 0):
                continue

            uniqueFilenames.append(msg.attachments[0].filename)
            imageMessages.append(msg.attachments[0].url)

        return imageMessages