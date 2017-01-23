from model.gameModel import *
from repository.sentenceRepository import *

class GameRepository():
    def __init__(self):
        self.__gameModel = Game()
        self.__currentSentence = SentenceRepository()
        self.__gameModel.setScore(self.__currentSentence.getState().getScoreWeight())

    def gameCompute(self):
            self.__gameModel.setStatus("running")
            currentSentenceState = self.__currentSentence.getState()
            print(self.toString( currentSentenceState.getSentenceScrambled()) + "[ score is: " + str(self.__gameModel.getScore()) + " ]" )

    def gameAnswer(self, cmd):
        try:
            if cmd[:4] != "swap":
                raise RuntimeError("command not found")

            #delete swap
            cmd = cmd[4:]
            cmd = cmd.split("-")

            part1 = cmd[0].strip().split(" ")
            part2 = cmd[1].strip().split(" ")

            word1 = int(part1[0])
            letter1 = int(part1[1])

            word2 = int(part2[0])
            letter2 = int(part2[1])

            newSentence = self.__currentSentence.swap(self.__currentSentence.getState().getSentenceScrambled(), word1, letter1, word2, letter2)

            #Setting the new sentence
            self.__currentSentence.changeSentenceScrambled(newSentence)

            #Adjusting the score
            self.__gameModel.setScore( self.__gameModel.getScore() - 1)

        except Exception as e:
            print("Input not given properly")


    def checkGame(self):
        if self.__gameModel.getScore() == 0:
            self.__gameModel.setStatus("finished")
            self.__gameModel.setMessage("You lost !")
            print("You lost !")

        if self.__currentSentence.getState().getSentence() == self.__currentSentence.getState().getSentenceScrambled():
            self.__gameModel.setStatus("finished")
            self.__gameModel.setMessage("You won ! Your score is " + str(self.__gameModel.getScore()) )
            print("You won ! Your score is " + str(self.__gameModel.getScore()))

            raise RuntimeError("finished")

    def toString(self, lst):
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

    def getState(self):
        '''
        :return: the state object of type Game()
        '''
        return self.__gameModel

    def incrementScore(self):
        self.__gameModel.setScore( self.__gameModel.getScore() - 1 )