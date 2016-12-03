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

    def removeClient(self, client):
        '''
        :param client:  Client object
        :return:
        '''
        id = self._clientRepository.getClientIdByName(client.getName())
        self._rentalRepository.removeByClientId( id )
        self._clientRepository.removeClient(client)

    def replaceClient(self, clientOld, clientNew):
        oldId = self._clientRepository.getClientIdByName(clientOld.getName())
        clientOld.setManuallyClientId(oldId)

        self._clientRepository.replaceClient(clientOld, clientNew)
        self._rentalRepository.replaceClient(clientOld, clientNew)

    def removeMovie(self, movie):
        oldId = self._movieRepository.findMovie(movie)

        self._movieRepository.removeMovie(movie)
        self._rentalRepository.removeByMovieId(oldId)

    def replaceMovie(self, movieOld, movieNew):
        oldId = self._movieRepository.findMovie(movieOld)

        movieOld.setManuallyMovieId(oldId)
        self._movieRepository.replaceMovie(movieOld, movieNew)
        self._rentalRepository.replaceMovie(movieOld, movieNew)