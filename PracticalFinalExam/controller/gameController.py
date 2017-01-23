from model.gameModel import *
from repository.gameRepository import *
import copy

class GameController():
    def __init__(self):
        self.__gameRepository = GameRepository()
        self.__lastState = []
        self.gameComputeMain()

    def gameComputeMain(self):
        while self.__gameRepository.getState().getStatus() != "finished":
            self.__gameRepository.checkGame()
            self.__gameRepository.gameCompute()

            if self.__gameRepository.getState().getStatus() != "finished":
                cmd = input("Command: ")
                if cmd != "undo":
                    self.__lastState = copy.deepcopy(self.__gameRepository)
                    self.__gameRepository.gameAnswer(cmd)
                else:
                    self.undo()
                    self.__gameRepository.incrementScore()

    def undo(self):
        if self.__lastState == []:
            print("Can't undo")
        else:
            self.__gameRepository = self.__lastState
            self.__lastState = []

