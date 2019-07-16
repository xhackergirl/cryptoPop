import cryptomath, detectEnglish, freqAnalysis, makeWordPatterns, paperclip, wordPatterns
import os, re, sys
#from module import cryptomath, detectEnglish, freqAnalysis, makeWordPatterns, paperclip, wordPattern
print('choose a number: ')
print("""
1- Ceasar cipher
2- Reverse Cipher
3- Transposition Cipher
4- Affine Cipher
5- Simple Substitution Cipher
6- Vigenere Cipher
7- Public Key Cipher
8- Atbash cipher
9- ROT13 Cipher
note: dont use numbers 4 and 7, i am still fixing them
""")
nb = int(input('> '))

if nb == 1 or nb == 9:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    print('You have chosen the Ceasar Cipher! You want to: ')
    if nb == 1:
        print("""
        1- encrypt
        2- decrypt (with a key)
        3- decrypt (with no key)
        4- encrypt a file
        5- decrypt a file (with a key)
        6- decrypt a file (with no key)
        """)
    elif nb == 9:
        print("""
        1- encrypt
        2- decrypt 
        4- encrypt a file
        5- decrypt a file
        """)

    a = int(input('> '))
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
     

    if a == 1 or a == 2:
        def main():
            myMessage = input('enter your message: ')
            if nb == 1:
                myKey = int(input('enter the key: '))
            elif nb == 9:
                myKey = 13
            if a == 1:
                myMode = 'encrypt'
                
            if a == 2:
                myMode = 'decrypt'

            if myMode == 'encrypt':
                translated = encryptMessage(myKey, myMessage)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, myMessage)
            print('Key: %s' % (myKey))
            print('%sed text:' % (myMode.title()))
            print(translated)
            #paperclip.copy(translated)
            #print('Full %sed text copied to clipboard.' % (myMode))

    def encryptordecrypt(key, message, mode):
        translated = ''

        for symbol in message:

            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                
                if a == 1:
                    mode == 'encrypt'

                elif a == 2:
                    mode == 'decrypt'
        
                if mode == 'encrypt':
                    translatedIndex = symbolIndex + key
                    
                       
                elif mode == 'decrypt':
                    
                    translatedIndex = symbolIndex - key
 
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
        
                translated = translated + symbol

        return translated
        
    def encryptMessage(key, message):
        return encryptordecrypt(key, message, 'encrypt')

    def decryptMessage(key, message):
        return encryptordecrypt(key, message, 'decrypt')
    if a == 3:
        def main():
    
            myMessage = input('enter a message: ')

            hackedMessage = hackCeasar(myMessage)
            #print(hackedMessage)

            """if hackedMessage != None:
                
                print('Copying hacked message to clipboard:')
                print(hackedMessage)
                paperclip.copy(hackedMessage)
            else:
                print('Failed to hack encryption.')"""
    
    def hackCeasar(message):
        for key in range(len(SYMBOLS)): 
            translated = ''

            for symbol in message:
                if symbol in SYMBOLS:
                    symbolIndex =SYMBOLS.find(symbol) 

        
                    translatedIndex = symbolIndex - key

    
                    if translatedIndex < 0:
                        translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]

            else:
                translated = translated + symbol
            if detectEnglish.isEnglish(translated):
            # Ask user if this is the correct decryption.
                print()
                print('Possible encryption hack:')
                print('Key %s: %s' % (key, translated[:100]))
                print()
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')

                if response.strip().upper().startswith('D'):
                    print('the decrypted text is: ', translated)
                    

                return translated
    if a == 4 or a == 5:
        def main():
            inputFilename = input('enter the file name: ')
    
            if nb == 1:
                myKey = int(input('enter a key: '))
            elif nb == 9:
                myKey = 13
            if a == 4:
                myMode = 'encrypt'
                    
            elif a == 5:
                myMode = 'decrypt'

            outputFilename = '%s.%sed.txt' % (inputFilename.replace('.txt', ''), myMode)
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting...' % (inputFilename))
                sys.exit()

    
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

    
            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()

            print('%sing...' % (myMode.title()))

    
            startTime = time.time()
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, content)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, content)
            totalTime = round(time.time() - startTime, 2)
            print('%sion time: %s seconds' % (myMode.title(), totalTime))

    
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(translated)
            outputFileObj.close()

            print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
            print('%sed file is %s.' % (myMode.title(), outputFilename))

    if a == 6:
        def main():
            inputFilename = input('enter the file name: ')
            outputFilename = '%s.decrypted.txt' % (inputFilename.replace('.txt', ''))
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting.' % (inputFilename))
                sys.exit()

            inputFile = open(inputFilename)
            content = inputFile.read()
            inputFile.close()

            hackedMessage = hackCeasar(content)

            if hackedMessage != None:
                print('Writing decrypted text to %s.' % (outputFilename))

                outputFile = open(outputFilename, 'w')
                outputFile.write(hackedMessage)
                outputFile.close()
            else:
                print('Failed to hack encryption.')
    if __name__ == '__main__':
        main()
if nb == 2:
    print('you chose the reverse cipher!')
    print('please enter your message: ')
    message = input()
    print('''
    you want to:
    1- encrypt
    2- decrypt
    ''')
    a = int(input('> '))
    if a == 1:
        mode = 'encrypt'
    elif a == 2:
        mode = 'decrypt'
    else:
        print('invalid output')
        sys.exit()
    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    print('the %sed message is: \n%s' % (mode, translated))
if nb == 3:
    print('You have chosen the transposition Cipher! You want to: ')
    print("""
    1- encrypt
    2- decrypt (with a key)
    3- decrypt (with no key)
    4- encrypt a file
    5- decrypt a file (with a key)
    6- decrypt a file (with no key)
    """)
    a = int(input('> '))
    
        
    if a == 1: 
        def main():
            mymessage = input("enter message: ")
            mykey = int(input("enter key: "))

            ciphertext = encryptMessage(mykey, mymessage)

            print(ciphertext +'|')
    if a == 4 or a == 5:
        def main():
            inputFilename = input('enter the file name: ')
    
            
            myKey = int(input('enter a key: '))
            if a == 4:
                myMode = 'encrypt'
                    
            elif a == 5:
                myMode = 'decrypt'

            outputFilename = '%s.%sed.txt' % (inputFilename.replace('.txt', ''), myMode)
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting...' % (inputFilename))
                sys.exit()

    
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

    
            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()

            print('%sing...' % (myMode.title()))

    
            startTime = time.time()
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, content)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, content)
            totalTime = round(time.time() - startTime, 2)
            print('%sion time: %s seconds' % (myMode.title(), totalTime))

    
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(translated)
            outputFileObj.close()

            print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
            print('%sed file is %s.' % (myMode.title(), outputFilename))


    def encryptMessage(key, message):
        ciphertext = [''] * key

        for column in range(key):
            currentIndex = column

            while currentIndex < len(message):
                ciphertext[column] += message[currentIndex]

                currentIndex += key

        return ''.join(ciphertext) 
        
    if a == 2:
        def main():
            print('enter a message: ')
            myMessage = input()
            print('enter a key: ')
            myKey = int(input('> '))

            plaintext = decryptMessage(myKey, myMessage)

            print(plaintext + '|')

    def decryptMessage(key, message):
        numOfColumns = int(math.ceil(len(message) / float(key)))
    
        numOfRows = key
    
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    
        plaintext = [''] * numOfColumns

    
        column = 0
        row = 0

        for symbol in message:
            plaintext[column] += symbol
            column += 1 

        
            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1

        return ''.join(plaintext)

        
    if a == 3:
        def main():
    
            myMessage = input('enter the cipher text: ')

            hackedMessage = hackTransposition(myMessage)

            if hackedMessage == None:
                print('Failed to hack encryption.')
            else:
                print('Copying hacked message to clipboard:')
                print(hackedMessage)
                paperclip.copy(hackedMessage)

    def hackTransposition(message):
        print('Hacking...')

    
        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    
        for key in range(1, len(message)):
            print('Trying key #%s...' % (key))
            sys.stdout.flush()
            startTime = time.time()
            decryptedText = decryptMessage(key, message)
            englishPercentage = round(detectEnglish.getEnglishCount(decryptedText) * 100, 2)


            totalTime = round(time.time() - startTime, 3)
            print('Test time: %s seconds, ' % (totalTime), end='')
            sys.stdout.flush() 

            print('Percent English: %s%%' % (englishPercentage))
            if englishPercentage > 20:
                print()
                print('Key ' + str(key) + ': ' + decryptedText[:100])
                print()
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')
                if response.strip().upper().startswith('D'):
                    return decryptedText
        return None

    if a == 6:
        def main():
            inputFilename = input('enter the file name: ')
            outputFilename = '%s.decrypted.txt' % (inputFilename.replace('.txt', ''))
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting.' % (inputFilename))
                sys.exit()

            inputFile = open(inputFilename)
            content = inputFile.read()
            inputFile.close()

            hackedMessage = hackTransposition(content)

            if hackedMessage != None:
                print('Writing decrypted text to %s.' % (outputFilename))

                outputFile = open(outputFilename, 'w')
                outputFile.write(hackedMessage)
                outputFile.close()
            else:
                print('Failed to hack encryption.')

                

    if __name__ == '__main__':
        main()
if nb == 4:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    print('''
    do you want to:
    1- encrypt
    2- decrypt (with a key)
    3- decrypt (with no key)
    4- encrypt a file
    5- decrypt a file (with a key)
    6- decrypt a file (with no key)
    ''')
    a = int(input('> '))
    if a == 1 or a == 2:
        def main():
            myMessage = input('enter your message: ')
            myKey = int(input('enter the key: '))
            if a == 1:
                myMode = 'encrypt'
                
            if a == 2:
                myMode = 'decrypt'

            if myMode == 'encrypt':
                translated = encryptMessage(myKey, myMessage)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, myMessage)
            print('Key: %s' % (myKey))
            print('%sed text:' % (myMode.title()))
            print(translated)
            paperclip.copy(translated)
            print('Full %sed text copied to clipboard.' % (myMode))

    if a == 3:
        def main():
    
            myMessage = input('enter a message')

            hackedMessage = hackAffine(myMessage)

            if hackedMessage != None:
                
                print('Copying hacked message to clipboard:')
                print(hackedMessage)
                paperclip.copy(hackedMessage)
            else:
                print('Failed to hack encryption.')

    if a == 4 or a == 5:
        def main():
            inputFilename = input('enter the file name: ')
    
            
            myKey = int(input('enter a key: '))
            if a == 4:
                myMode = 'encrypt'
                    
            elif a == 5:
                myMode = 'decrypt'

            outputFilename = '%s.%sed.txt' % (inputFilename.replace('.txt', ''), myMode)
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting...' % (inputFilename))
                sys.exit()

    
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

    
            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()

            print('%sing...' % (myMode.title()))

    
            startTime = time.time()
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, content)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, content)
            totalTime = round(time.time() - startTime, 2)
            print('%sion time: %s seconds' % (myMode.title(), totalTime))

    
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(translated)
            outputFileObj.close()

            print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
            print('%sed file is %s.' % (myMode.title(), outputFilename))

    if a == 6:
        def main():
            inputFilename = input('enter the file name: ')
            outputFilename = '%s.decrypted.txt' % (inputFilename.replace('.txt', ''))
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting.' % (inputFilename))
                sys.exit()

            inputFile = open(inputFilename)
            content = inputFile.read()
            inputFile.close()

            hackedMessage = hackAffine(content)

            if hackedMessage != None:
                print('Writing decrypted text to %s.' % (outputFilename))

                outputFile = open(outputFilename, 'w')
                outputFile.write(hackedMessage)
                outputFile.close()
            else:
                print('Failed to hack encryption.')

    def hackAffine(message):
        print('Hacking...')

        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

        for key in range(len(SYMBOLS) ** 2):
            keyA = getKeyParts(key)[0]
            if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
                continue

            decryptedText = decryptMessage(key, message)
            if not SILENT_MODE:
                print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

            if detectEnglish.isEnglish(decryptedText):
                
                print()
                print('Possible encryption hack:')
                print('Key: %s' % (key))
                print('Decrypted message: ' + decryptedText[:200])
                print()
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')

                if response.strip().upper().startswith('D'):
                    return decryptedText
        return None
  
    def getKeyParts(key):
        keyA = key // len(SYMBOLS)
        keyB = key % len(SYMBOLS)
        return (keyA, keyB)


    def checkKeys(keyA, keyB, mode):
        if keyA == 1 and mode == 'encrypt':
            sys.exit('Cipher is weak if key A is 1. Choose a different key.')
        if keyB == 0 and mode == 'encrypt':
            sys.exit('Cipher is weak if key B is 0. Choose a different key.')
        if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
            sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
        if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
            sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


    def encryptMessage(key, message):
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA, keyB, 'encrypt')
        ciphertext = ''
        for symbol in message:
            if symbol in SYMBOLS:
                # Encrypt the symbol:
                symbolIndex = SYMBOLS.find(symbol)
                ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
            else:
                ciphertext += symbol # Append the symbol without encrypting.
        return ciphertext


    def decryptMessage(key, message):
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA, keyB, 'decrypt')
        plaintext = ''
        modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

        for symbol in message:
            if symbol in SYMBOLS:
                # Decrypt the symbol:
                symbolIndex = SYMBOLS.find(symbol)
                plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
            else:
                plaintext += symbol # Append the symbol without decrypting.
        return plaintext



    if __name__ == '__main__':
        main()
# there is a big problem in number 4
if nb == 5:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('You have chosen the Simple Substitution Cipher! You want to: ')
    print("""
    1- encrypt
    2- decrypt (with a key)
    3- decrypt (with no key)
    4- encrypt a file
    5- decrypt a file (with a key)
    6- decrypt a file (with no key)
    """)
    a = int(input('> '))
    if a == 1 or a == 2:
        def main():
            myMessage = input('enter a message: ')
            myKey = input('enter a key (for example: LFWOAYUISVKMNXPBDCRJTQEGHZ): ')
            if a == 1:
                myMode = 'encrypt' 
            elif a == 2:
                myMode = 'decrypt'

            if not keyIsValid(myKey):
                sys.exit('There is an error in the key or symbol set.')
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, myMessage)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, myMessage)
            print('Using key %s' % (myKey))
            print('The %sed message is:' % (myMode))
            print(translated)
            paperclip.copy(translated)
            print()
            print('This message has been copied to the clipboard.')

    if a == 4 or a == 5:
        def main():
            inputFilename = input('enter the file name: ')
    
            
            myKey = input('enter a key: ')
            if a == 4:
                myMode = 'encrypt'
                    
            elif a == 5:
                myMode = 'decrypt'

            outputFilename = '%s.%sed.txt' % (inputFilename.replace('.txt', ''), myMode)
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting...' % (inputFilename))
                sys.exit()

    
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()

            print('%sing...' % (myMode.title()))

    
            startTime = time.time()
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, content)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, content)
            totalTime = round(time.time() - startTime, 2)
            print('%sion time: %s seconds' % (myMode.title(), totalTime))

    
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(translated)
            outputFileObj.close()

            print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
            print('%sed file is %s.' % (myMode.title(), outputFilename))


    if a == 6:
        def main():
            inputFilename = input('enter the file name: ')
            outputFilename = '%s.decrypted.txt' % (inputFilename.replace('.txt', ''))
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting.' % (inputFilename))
                sys.exit()

            inputFile = open(inputFilename)
            content = inputFile.read()
            inputFile.close()

            letterMapping = hackSimpleSub(content)
            hackedMessage = decryptWithCipherletterMapping(content, letterMapping)

            if hackedMessage != None:
                print('Writing decrypted text to %s.' % (outputFilename))

                outputFile = open(outputFilename, 'w')
                outputFile.write(hackedMessage)
                outputFile.close()
            else:
                print('Failed to hack encryption.')    
    
    def keyIsValid(key):
        keyList = list(key)
        lettersList = list(LETTERS)
        keyList.sort()
        lettersList.sort()

        return keyList == lettersList


    def encryptMessage(key, message):
        return translateMessage(key, message, 'encrypt')


    def decryptMessage(key, message):
        return translateMessage(key, message, 'decrypt')


    def translateMessage(key, message, mode):
        translated = ''
        charsA = LETTERS
        charsB = key
        if mode == 'decrypt':
            charsA, charsB = charsB, charsA

        for symbol in message:
            if symbol.upper() in charsA:
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                translated += symbol

        return translated
    nonLettersOrSpacePattern = re.compile('[^A-Z\s]')
    if a == 3:
        def main():
            message = input('enter your message: ')
            print('Hacking...')
            letterMapping = hackSimpleSub(message)

            print('Mapping:')
            print(letterMapping)
            print()
            print('Original ciphertext:')
            print(message)
            print()
            print('Copying hacked message to clipboard:')
            hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
            paperclip.copy(hackedMessage)
            print(hackedMessage)

    def getBlankCipherletterMapping():
        return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


    def addLettersToMapping(letterMapping, cipherword, candidate):
        for i in range(len(cipherword)):
            if candidate[i] not in letterMapping[cipherword[i]]:
                letterMapping[cipherword[i]].append(candidate[i])



    def intersectMappings(mapA, mapB):
        intersectedMapping = getBlankCipherletterMapping()
        for letter in LETTERS:

            if mapA[letter] == []:
                intersectedMapping[letter] = copy.deepcopy(mapB[letter])
            elif mapB[letter] == []:
                intersectedMapping[letter] = copy.deepcopy(mapA[letter])
            else:
                for mappedLetter in mapA[letter]:
                    if mappedLetter in mapB[letter]:
                        intersectedMapping[letter].append(mappedLetter)

        return intersectedMapping


    def removeSolvedLettersFromMapping(letterMapping):
        loopAgain = True
        while loopAgain:
            loopAgain = False

            solvedLetters = []
            for cipherletter in LETTERS:
                if len(letterMapping[cipherletter]) == 1:
                    solvedLetters.append(letterMapping[cipherletter][0])

            for cipherletter in LETTERS:
                for s in solvedLetters:
                    if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                        letterMapping[cipherletter].remove(s)
                        if len(letterMapping[cipherletter]) == 1:
                            loopAgain = True
        return letterMapping


    def hackSimpleSub(message):
        intersectedMap = getBlankCipherletterMapping()
        cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
        for cipherword in cipherwordList:
            candidateMap = getBlankCipherletterMapping()

            wordPattern = makeWordPatterns.getWordPattern(cipherword)
            if wordPattern not in wordPatterns.allPatterns:
                continue 
                
            for candidate in wordPatterns.allPatterns[wordPattern]:
                addLettersToMapping(candidateMap, cipherword, candidate)

            intersectedMap = intersectMappings(intersectedMap, candidateMap)

        
        return removeSolvedLettersFromMapping(intersectedMap)


    def decryptWithCipherletterMapping(ciphertext, letterMapping):
        
        key = ['x'] * len(LETTERS)
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                
                keyIndex = LETTERS.find(letterMapping[cipherletter][0])
                key[keyIndex] = cipherletter
            else:
                ciphertext = ciphertext.replace(cipherletter.lower(), '_')
                ciphertext = ciphertext.replace(cipherletter.upper(), '_')
        key = ''.join(key)

        
        return decryptMessage(key, ciphertext)


    if __name__ == '__main__':
        main()
if nb == 6:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SILENT_MODE = False 
    NUM_MOST_FREQ_LETTERS = 4 
    MAX_KEY_LENGTH = 16 
    NONLETTERS_PATTERN = re.compile('[^A-Z]')
    print('''
    do you want to:
    1- encrypt
    2- decrypt (with a key)
    3- decrypt (with no key)
    4- encrypt a file
    5- decrypt a file (with a key)
    6- decrypt a file (with no key)
    ''')
    a = int(input('> '))
    if a == 1 or a == 2:
        def main():
    
            myMessage = input('enter your message: ')
            myKey = input('enter the key (for example: ASIMOV): ')
            if a == 1:
                myMode = 'encrypt' 
            elif a == 2:
                myMode = 'decrypt'

            if myMode == 'encrypt':
                translated = encryptMessage(myKey, myMessage)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, myMessage)

            print('%sed message:' % (myMode.title()))
            print(translated)
            paperclip.copy(translated)
            print()
            print('The message has been copied to the clipboard.')

    if a == 3:
        def main():
    
            ciphertext = input('enter the cipher text: ')
            hackedMessage = hackVigenere(ciphertext)

            if hackedMessage != None:
                print('Copying hacked message to clipboard:')
                print(hackedMessage)
                paperclip.copy(hackedMessage)
            else:
                print('Failed to hack encryption.')


    if a == 4 or a == 5:
        def main():
            inputFilename = input('enter the file name: ')
    
            
            myKey = input('enter a key: ')
            if a == 4:
                myMode = 'encrypt'
                    
            elif a == 5:
                myMode = 'decrypt'

            outputFilename = '%s.%sed.txt' % (inputFilename.replace('.txt', ''), myMode)
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting...' % (inputFilename))
                sys.exit()

    
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

    
            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()

            print('%sing...' % (myMode.title()))

    
            startTime = time.time()
            if myMode == 'encrypt':
                translated = encryptMessage(myKey, content)
            elif myMode == 'decrypt':
                translated = decryptMessage(myKey, content)
            totalTime = round(time.time() - startTime, 2)
            print('%sion time: %s seconds' % (myMode.title(), totalTime))

    
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(translated)
            outputFileObj.close()

            print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
            print('%sed file is %s.' % (myMode.title(), outputFilename))

    if a == 6:
        def main():
            inputFilename = input('enter the file name: ')
            outputFilename = '%s.decrypted.txt' % (inputFilename.replace('.txt', ''))
            if not os.path.exists(inputFilename):
                print('The file %s does not exist. Quitting.' % (inputFilename))
                sys.exit()

            inputFile = open(inputFilename)
            content = inputFile.read()
            inputFile.close()

            hackedMessage = hackVigenere(content)

            if hackedMessage != None:
                print('Writing decrypted text to %s.' % (outputFilename))

                outputFile = open(outputFilename, 'w')
                outputFile.write(hackedMessage)
                outputFile.close()
            else:
                print('Failed to hack encryption.')

    def encryptMessage(key, message):
        return translateMessage(key, message, 'encrypt')


    def decryptMessage(key, message):
        return translateMessage(key, message, 'decrypt')


    def translateMessage(key, message, mode):
        translated = [] # Stores the encrypted/decrypted message string.

        keyIndex = 0
        key = key.upper()

        for symbol in message: # Loop through each symbol in message.
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS.
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex]) # Add if encrypting.
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting.

                num %= len(LETTERS) # Handle any wraparound.

                # Add the encrypted/decrypted symbol to the end of translated:
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Append the symbol without encrypting/decrypting.
                translated.append(symbol)

        return ''.join(translated)

    def findRepeatSequencesSpacings(message):
    
        message = NONLETTERS_PATTERN.sub('', message.upper())

    
        seqSpacings = {} 
        for seqLen in range(3, 6):
            for seqStart in range(len(message) - seqLen):
                
                seq = message[seqStart:seqStart + seqLen]

                
                for i in range(seqStart + seqLen, len(message) - seqLen):
                    if message[i:i + seqLen] == seq:
                        
                        if seq not in seqSpacings:
                            seqSpacings[seq] = []
                        seqSpacings[seq].append(i - seqStart)
        return seqSpacings


    def getUsefulFactors(num):
        

        if num < 2:
            return [] 

        factors = [] 

        for i in range(2, MAX_KEY_LENGTH + 1): 
            if num % i == 0:
                factors.append(i)
                otherFactor = int(num / i)
                if otherFactor < MAX_KEY_LENGTH + 1 and otherFactor != 1:
                    factors.append(otherFactor)
        return list(set(factors)) 


    def getItemAtIndexOne(items):
        return items[1]


    def getMostCommonFactors(seqFactors):
        
        factorCounts = {} 
        
        for seq in seqFactors:
            factorList = seqFactors[seq]
            for factor in factorList:
                if factor not in factorCounts:
                    factorCounts[factor] = 0
                factorCounts[factor] += 1

        
        factorsByCount = []
        for factor in factorCounts:
            
            if factor <= MAX_KEY_LENGTH:
                
                factorsByCount.append( (factor, factorCounts[factor]) )

        
        factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

        return factorsByCount


    def kasiskiExamination(ciphertext):
        
        repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

        
        seqFactors = {}
        for seq in repeatedSeqSpacings:
            seqFactors[seq] = []
            for spacing in repeatedSeqSpacings[seq]:
                seqFactors[seq].extend(getUsefulFactors(spacing))

        
        factorsByCount = getMostCommonFactors(seqFactors)

        
        allLikelyKeyLengths = []
        for twoIntTuple in factorsByCount:
            allLikelyKeyLengths.append(twoIntTuple[0])

        return allLikelyKeyLengths


    def getNthSubkeysLetters(nth, keyLength, message):
        
        message = NONLETTERS_PATTERN.sub('', message)

        i = nth - 1
        letters = []
        while i < len(message):
            letters.append(message[i])
            i += keyLength
        return ''.join(letters)


    def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
        
        ciphertextUp = ciphertext.upper()
        
        allFreqScores = []
        for nth in range(1, mostLikelyKeyLength + 1):
            nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

           
            freqScores = []
            for possibleKey in LETTERS:
                decryptedText = decryptMessage(possibleKey, nthLetters)
                keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
                freqScores.append(keyAndFreqMatchTuple)
            
            freqScores.sort(key=getItemAtIndexOne, reverse=True)

            allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

        if not SILENT_MODE:
            for i in range(len(allFreqScores)):
                # Use i + 1 so the first letter is not called the "0th" letter:
                print('Possible letters for letter %s of the key: ' % (i + 1), end='')
                for freqScore in allFreqScores[i]:
                    print('%s ' % freqScore[0], end='')
                print() # Print a newline.

        # Try every combination of the most likely letters for each position
        # in the key:
        for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
            # Create a possible key from the letters in allFreqScores:
            possibleKey = ''
            for i in range(mostLikelyKeyLength):
                possibleKey += allFreqScores[i][indexes[i]][0]

            if not SILENT_MODE:
                print('Attempting with key: %s' % (possibleKey))

            decryptedText = decryptMessage(possibleKey, ciphertextUp)

            if detectEnglish.isEnglish(decryptedText):
                # Set the hacked ciphertext to the original casing:
                origCase = []
                for i in range(len(ciphertext)):
                    if ciphertext[i].isupper():
                        origCase.append(decryptedText[i].upper())
                    else:
                        origCase.append(decryptedText[i].lower())
                decryptedText = ''.join(origCase)

                
                print('Possible encryption hack with key %s:' % (possibleKey))
                print(decryptedText[:200]) 
                print()
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')

                if response.strip().upper().startswith('D'):
                    return decryptedText

        return None


    def hackVigenere(ciphertext):
        allLikelyKeyLengths = kasiskiExamination(ciphertext)
        if not SILENT_MODE:
            keyLengthStr = ''
            for keyLength in allLikelyKeyLengths:
                keyLengthStr += '%s ' % (keyLength)
            print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')
        hackedMessage = None
        for keyLength in allLikelyKeyLengths:
            if not SILENT_MODE:
                print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
            hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
            if hackedMessage != None:
                break

        
        if hackedMessage == None:
            if not SILENT_MODE:
                print('Unable to hack message with likely key length(s). Brute forcing key length...')
            for keyLength in range(1, MAX_KEY_LENGTH + 1):
                
                if keyLength not in allLikelyKeyLengths:
                    if not SILENT_MODE:
                        print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                    hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                    if hackedMessage != None:
                        break
        return hackedMessage

    if __name__ == '__main__':
        main()

#if nb == 8:
# he Atbash cipher is also an Affine cipher with a=25 and b = 25





