class UI():
    def __init__(self, gameController):
        self.__gameController = gameController

    def toPrint(self, msg):
        '''
        :param msg: string message to be printed
        :return: nothing, it justs print
        '''
        print(msg)

    def convertToBePrinted(self, lst):
        '''
        :param lst: a word list
        :return: a string nicely formated to be printed
        '''
        res = ""
        for word in lst:
            for letter in word:
                res += letter

            res += " "

        return res
