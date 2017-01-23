import random
from model.sentenceModel import *

class SentenceRepository():
    def __init__(self):
        self.__state = SentenceModel()
        self.__state.setSentence(self.parseSentence(self.loadSentence()))
        self.__state.setScoreWeight(self.countLetters(self.__state.getSentence()))
        self.__state.setSentenceScrambled(self.scramble(self.__state.getSentence()))
        a = 3


    def loadSentence(self):
        '''
        :return: generates a random sentence line from the file and returns it
        '''
        maxLines = crtLine = chosenLine = 0

        with open('/Users/so/Desktop/ExamenFp/data/sentence.txt') as file:
            for line in file:
                maxLines += 1

        chosenLine = random.randint(0, maxLines - 1)

        with open('/Users/so/Desktop/ExamenFp/data/sentence.txt') as file:
            for line in file:
                if crtLine == chosenLine:
                        return line.replace("\n", "")

                crtLine += 1

    def parseSentence(self, sentence):
        '''
        :param sentence: a string containing the chosen sentence
        :return: a list with all the words parsed
        '''
        return sentence.split(' ')

    def countLetters(self, sentence):
        '''
        :param sentence: a list containing all the words
        :return: an integer representing the number of letters
        '''
        res = 0
        for crt in sentence:
            res += len(crt)

        return res

    def scramble(self, sentence):
        '''
        :param sentence: a list containing all the words
        :return: the same list with the sentence scrambled
        '''

        numberOfTimes = random.randint(1, 10)

        for i in range(numberOfTimes):
            try:
                word1 = random.randint(1, len(sentence) - 1)
                letter1 = random.randint(1, len(sentence[word1]) - 2)

                word2 = random.randint(1, len(sentence) - 1)
                letter2 = random.randint(1, len(sentence[word2]) - 2)

                if word1 == word2:
                    while letter2 == letter1:
                        letter2 = random.randint(0, len(sentence[word2]) - 2)

                sentence = self.swap(sentence, word1, letter1, word2, letter2)
            except Exception as e:
                pass

        return sentence

    def swap(self, sentence, word1, letter1, word2, letter2):
        '''
        :param sentence: list of words
        :param word1: integer
        :param letter1: integer
        :param word2: integer
        :param letter2: integer
        :return: the list with the position swapped
        '''
        res = []

        if word1 >= len(sentence) or word1 < 0 or word2 >= len(sentence) or word2 < 0:
            print("Invalid indexes were provided")
            return sentence

        if letter1 >= len(sentence[word1]) or letter1 < 0 or letter2 >= len(sentence[word2]) or letter2 < 0:
            print("Invalid indexes were provided")
            return sentence

        for i in range(len(sentence)):
            newStr = ""

            for j in range(len(sentence[i])):
                if word1 == i and j == letter1:
                    newStr += sentence[word2][letter2]
                else:
                    if word2 == i and j == letter2:
                        newStr += sentence[word1][letter1]
                    else:
                        newStr += sentence[i][j]

            res.append(newStr)

        return res

    def getState(self):
        '''
        :return: the state object of type SentenceModel
        '''
        return self.__state

    def changeSentenceScrambled(self, str):
        '''
        :param str: list with the new sentence
        '''
        self.__state.setSentenceScrambled(str)