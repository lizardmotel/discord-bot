from DictionaryQueryHandler import DictionaryQueryHandler

class MessageHandler:
    def __init__(self):
        self.dictionaryQueryHandler = DictionaryQueryHandler()

    def getReturnMessage(self, message):
        query = message.content

        if not query or not isinstance(query, str):
            return ''

        return self.handleQuery(query)

    def handleQuery(self, query):
        if query.startswith('deez'):
            return 'nuts'

        if query.startswith('define'):
            return self.dictionaryQueryHandler.getDefinition(query)

        return None
