from DictionaryQueryHandler import DictionaryQueryHandler
from ImageHandler import ImageHandler

class MessageHandler:
    def __init__(self):
        self.dictionaryQueryHandler = DictionaryQueryHandler()
        self.imageHandler = ImageHandler()


    def getReturnMessage(self, message, messageList):
        query = message.content

        if not query or not isinstance(query, str):
            return ''

        return self.handleQuery(query, messageList)

    def handleQuery(self, query, messageList):
        if query.startswith('deez'):
            return 'nuts'

        if query.startswith('define'):
            return self.dictionaryQueryHandler.getDefinition(query)

        if query.startswith('snap'):
            return self.imageHandler.sendImage(messageList)

        return None
