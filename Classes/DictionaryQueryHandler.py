import requests
import json

class DictionaryQueryHandler:
    def getDefinition(self, sentence):
        word = self.getFirstWordFromSentence(sentence)
        definition = None

        if word:
            definition = self.defineWord(word)

        return definition if definition else '%s does not exist' % (word)

    def getFirstWordFromSentence(self, sentence):
        splitSentence = sentence.split()

        return splitSentence[1] if len(splitSentence) > 1 else None

    def defineWord(self, word):
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/%s" % word)

        if response.status_code != 200:
            return

        responseData = json.loads(response.text)
        meaning = self.getMeaningFromResponseData(responseData)

        return meaning

    def getMeaningFromResponseData(self, responseData):
        meanings = responseData[0]['meanings']
        meaningString = ''

        for meaning in meanings:
            meaningString += meaning['definitions'][0]['definition'] + '\n'

        return meaningString