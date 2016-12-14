import copy
from movieRental.Repository.movieRepository import *
from movieRental.Repository.clientRepository import *
from movieRental.Repository.rentalRepository import *
from movieRental.Repository.fileRepository import *
from movieRental.Repository.jsonRepository import *
from movieRental.Repository.binaryRepository import *

__author__ = 'sorynsoo'

class MainController():
    def __init__(self, settings):
        '''
            Instantiates Movie, Client and Rental repositories
        '''
        self._stateIndex = 0
        self._state = []
        self._settingsObj = settings

        self._movieRepository = MovieRepository()
        self._clientRepository = ClientRepository()
        self._rentalRepository = RentalRepository()

        if self._settingsObj.getSettings("repository") == "file":
            self._dataSourceRepository = FileRepository()
        if self._settingsObj.getSettings("repository") == "pickle":
            self._dataSourceRepository = BinaryRepository()
        if self._settingsObj.getSettings("repository") == "json":
            self._dataSourceRepository = JsonRepository()


        self.loadFromRepository()


    def saveState(self, idOperation, object):
        '''
        :param idOperation: a string with operation identifier
        :param object: a Client or Movie object that has to be saved
        :return:
        '''
        self._state.append({"operation": idOperation, "object": object})

        self._stateIndex = len(self._state) - 1

    def saveToRepository(self):
        self._dataSourceRepository.save(self._clientRepository, "Client", self._settingsObj.getSettings("clientRepositoryPath"))
        self._dataSourceRepository.save(self._movieRepository, "Movie", self._settingsObj.getSettings("movieRepositoryPath"))
        self._dataSourceRepository.save(self._rentalRepository, "Rental", self._settingsObj.getSettings("rentalRepositoryPath"))

    def loadFromRepository(self):
        self._clientRepository._clientList =  self._dataSourceRepository.load("Client", self._settingsObj.getSettings("clientRepositoryPath"))
        self._movieRepository._movieList = self._dataSourceRepository.load("Movie", self._settingsObj.getSettings("movieRepositoryPath"))
        self._rentalRepository._rentalList = self._dataSourceRepository.load("Rental", self._settingsObj.getSettings("rentalRepositoryPath"))

    def undoState(self):
         '''
         :return: Self explinatory -> processes the operation of undo
         '''
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
        '''
            :return: Self explinatory -> processes the operation of redo
        '''
        if self._stateIndex == len(self._state) - 1:
            raise  RuntimeError("Can't redo anymore")

        self._stateIndex = self._stateIndex + 1;

        if (self._state[self._stateIndex]["operation"] == "addClient"):
            self._clientRepository.addClient(self._state[self._stateIndex]["object"])

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
        Removes a Client
        :param client:  Client object
        :return: nothing
        '''
        id = self._clientRepository.getClientIdByName(client.getName())
        self._rentalRepository.removeByClientId( id )
        self._clientRepository.removeClient(client)

    def replaceClient(self, clientOld, clientNew):
        '''
        :param clientOld: client object
        :param clientNew: client object
        :return: Replaces clientOld with clientNEw
        '''
        oldId = self._clientRepository.getClientIdByName(clientOld.getName())
        clientOld.setManuallyClientId(oldId)

        self._clientRepository.replaceClient(clientOld, clientNew)
        self._rentalRepository.replaceClient(clientOld, clientNew)

    def removeMovie(self, movie):
        '''
        :param movie: movie type Object
        :return: removes movie object
        '''
        oldId = self._movieRepository.findMovie(movie)

        self._movieRepository.removeMovie(movie)
        self._rentalRepository.removeByMovieId(oldId)

    def replaceMovie(self, movieOld, movieNew):
        '''
        :param movieOld: movie type Object
        :param movieNew: movie type Object
        :return: replaces movieOld with movieNew
        '''
        oldId = self._movieRepository.findMovie(movieOld)

        movieOld.setManuallyMovieId(oldId)
        self._movieRepository.replaceMovie(movieOld, movieNew)
        self._rentalRepository.replaceMovie(movieOld, movieNew)