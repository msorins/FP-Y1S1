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

    def saveState(self, idOperation, object):
        self._state.append({"operation": idOperation, "object": object})

        self._stateIndex = len(self._state) - 1

    def undoState(self):
         if self._stateIndex == 0:
             raise RuntimeError("Can't undo anymore")

         if(self._state[self._stateIndex]["operation"] == "addClient"):
             self.removeClient(self._state[self._stateIndex]["object"])

         if (self._state[self._stateIndex]["operation"] == "removeClient"):
             self._clientRepository.addClient(self._state[self._stateIndex]["object"])

         if (self._state[self._stateIndex]["operation"] == "replaceClient"):
             self.replaceClient(self._state[self._stateIndex]["object"]["newName"],
                                self._state[self._stateIndex]["object"]["oldName"])

         if (self._state[self._stateIndex]["operation"] == "addMovie"):
             self.removeMovie(self._state[self._stateIndex]["object"])

         if (self._state[self._stateIndex]["operation"] == "removeMovie"):
             self._movieRepository.addMovie(self._state[self._stateIndex]["object"])

         if (self._state[self._stateIndex]["operation"] == "replaceMovie"):
             self.replaceMovie(self._state[self._stateIndex]["object"]["newMovie"],
                                self._state[self._stateIndex]["object"]["oldMovie"])

         self._stateIndex = self._stateIndex - 1;

    def redoState(self):
        if self._stateIndex == len(self._state) - 1:
            raise  RuntimeError("Can't redo anymore")

        self._stateIndex = self._stateIndex + 1;

        if (self._state[self._stateIndex]["operation"] == "addClient"):
            self._clientRepository.addClient(self._state[self._stateIndex]["object"])
            self.removeClient(self._state[self._stateIndex]["object"])

        if (self._state[self._stateIndex]["operation"] == "removeClient"):
            self.removeClient(self._state[self._stateIndex]["object"])

        if (self._state[self._stateIndex]["operation"] == "replaceClient"):
            self.replaceClient(self._state[self._stateIndex]["object"]["oldName"],
                               self._state[self._stateIndex]["object"]["newName"])

        if (self._state[self._stateIndex]["operation"] == "addMovie"):
            self._movieRepository.addMovie(self._state[self._stateIndex]["object"])

        if (self._state[self._stateIndex]["operation"] == "removeMovie"):
            self.removeMovie(self._state[self._stateIndex]["object"])

        if (self._state[self._stateIndex]["operation"] == "replaceMovie"):
            self.replaceMovie(self._state[self._stateIndex]["object"]["oldMovie"],
                              self._state[self._stateIndex]["object"]["newMovie"])

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