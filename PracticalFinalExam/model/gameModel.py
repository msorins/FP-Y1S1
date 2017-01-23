class Game():
    def __init__(self):
        '''
        INIT FUNCTION
        '''
        self.__score = 0
        self.__message = ""
        self.__status = "firstTime"

    def getScore(self):
        '''
        :return: the value of the score
        '''
        return self.__score

    def setScore(self, score):
        '''
        :param score: int
        set msg to the __message
        '''
        self.__score = score

    def getMessage(self):
        '''
        :return: self.__message
        '''
        return self.__message

    def setMessage(self, msg):
        '''
        :param msg: a string
        :return: set msg to __message
        '''
        self.__message = msg

    def getStatus(self):
        '''
        :return: status property
        '''
        return self.__status

    def setStatus(self, status):
        '''
        :param status: string
        :return:
        '''

        self.__status = status

