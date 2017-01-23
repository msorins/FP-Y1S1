class SentenceModel():
    def __init__(self):
        self.__sentence = " "
        self.__sentenceScrambled = ""
        self.__scoreWeight = 0


    def getSentence(self):
        '''
        :return: the sentence
        '''
        return self.__sentence

    def setSentence(self, sentence):
        '''
        :param sentence: string
        set msg to the __sentence
        '''
        self.__sentence = sentence

    def getSentenceScrambled(self):
        '''
        :return: the sentence scrambled
        '''
        return self.__sentenceScrambled

    def setSentenceScrambled(self, sentence):
        '''
        :param sentence: string
        set msg to the __sentence
        '''
        self.__sentenceScrambled = sentence

    def getScoreWeight(self):
        '''
        :return: self.__score
        '''
        return self.__scoreWeight

    def setScoreWeight(self, score):
        '''
        :param msg: a string
        :return: set msg to __score
        '''
        self.__scoreWeight = score