# To use, type this code: 
# #   import detectEnglish 
# #   detectEnglish.isEnglish(someString) # 
# Returns True or False 
# # (There must be a "dictionary.txt" file in this directory with all 
# # English words in it, one word per line.

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
# split('\n') this means split whenever there is a new line
        englishWords[word] = None 
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # no words at all

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)

    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20 , letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch


