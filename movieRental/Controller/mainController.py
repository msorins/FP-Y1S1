import copy
from movieRental.Repository.movieRepository import *
from movieRental.Repository.clientRepository import *
from movieRental.Repository.rentalRepository import *
__author__ = 'sorynsoo'

class MainController():
    def __init__(self):
         self._movieRepository = MovieRepository()
         self._clientRepository = ClientRepository()
         self._rentalRepository = RentalRepository()

         self._stateIndex = 0
         self._state = []

    def saveState(self):
        movieControllerAux = copy.deepcopy(self._movieRepository)
        clientControllerAux = copy.deepcopy(self._clientRepository)
        rentalControllerAux = copy.deepcopy(self._rentalRepository)
        self._state.append({"movieController": movieControllerAux, "clientController": clientControllerAux, "rentalController": rentalControllerAux})

        self._stateIndex = len(self._state) -1

    def undoState(self):
         if self._stateIndex == 0:
             raise RuntimeError("Can't undo anymore")

         self._stateIndex = self._stateIndex - 1;
         self._movieRepository = self._state[self._stateIndex]["movieController"]
         self._clientRepository = self._state[self._stateIndex]["clientController"]
         self._rentalRepository = self._state[self._stateIndex]["rentalController"]

    def redoState(self):
        if self._stateIndex == len(self._state) - 1:
            raise  RuntimeError("Can't redo anymore")

        self._stateIndex = self._stateIndex + 1;
        self._movieRepository = self._state[self._stateIndex]["movieController"]
        self._clientRepository = self._state[self._stateIndex]["clientController"]
        self._rentalRepository = self._state[self._stateIndex]["rentalController"]