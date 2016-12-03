__author__ = 'sorynsoo'
from movieRental.Model.rental import *
import operator
import copy

class RentalRepository():
    def __init__(self):
        self._rentalList = []
        self._rentedMoviesCounter = {}
        self._rentedClientsCounter = {}
        self._state = []

    def rentMovie(self, rental):
        if not self.canUserRent(rental):
            raise RuntimeError("User cannot rent movie due to the fact that is untrustworty")
            return

        if(type(rental) == Rental):
            self._rentalList.append(rental)
            self.incrementRentedMoviesCounter(rental)
            self.incrementRentedClientsCounter(rental)
            #print(str(rental.getClientId()) + " request added to the rental log")
        else:
            raise TypeError("Invalid rental format")

    def returnMovie(self, rental):
        ok = False
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getMovieId() == rental.getMovieId():
                crt.setReturnedDate(rental.getReturnedDate())
                ok = True

        if ok != True:
            raise RuntimeError("Operation could not have been executed")

    def canUserRent(self, rental):
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getReturnedDate() != "" and crt.getReturnedDate() > crt.getDueDate():
                return False
        return True

    def mostRentedMovies(self):
        return sorted(self._rentedMoviesCounter.items(), key=operator.itemgetter(1), reverse = True)

    def mostActiveClients(self):
        return sorted(self._rentedClientsCounter.items(), key=operator.itemgetter(1), reverse = True)

    def rentalsAndMoviesCurrentlyRented(self):
        rtrn = {}

        for crt in self._rentalList:
            if crt.getReturnedDate() == "":
                if crt.getClientId() not in rtrn.keys():
                    rtrn[crt.getClientId()] = []
                    rtrn[crt.getClientId()].append(crt.getMovieId())
                else:
                    rtrn[crt.getClientId()].append(crt.getMovieId())

        return rtrn

    def currentlyRentedUnreturnedMovies(self):
        rtrn = []
        for crt in self._rentalList:
            if crt.getReturnedDate() == "":
                continue

            if crt.getReturnedDate() > crt.getDueDate():
                    rtrn.append(crt)

        auxObj = sorted(rtrn, key = lambda x: ((x.getReturnedDate() - x.getDueDate()).days), reverse = True)

        return auxObj

    def incrementRentedMoviesCounter(self, rental):
        if rental.getMovieId() in self._rentedMoviesCounter.keys():
            self._rentedMoviesCounter[rental.getMovieId()] = self._rentedMoviesCounter[rental.getMovieId()] + 1
        else:
            self._rentedMoviesCounter[rental.getMovieId()] = 1

    def getRentedMovieCounter(self, rental):
        return self._rentedMoviesCounter[rental.getMovieId()]

    def incrementRentedClientsCounter(self, rental):
        if rental.getClientId() in self._rentedClientsCounter.keys():
            self._rentedClientsCounter[rental.getClientId()] = self._rentedClientsCounter[rental.getClientId()] + 1
        else:
            self._rentedClientsCounter[rental.getClientId()] = 1

    def getRentedClientsCounter(self, rental):
        return self._rentedClientsCounter[rental.getClientId()]

    def removeByClientId(self, clientId):
        i = 0
        while i < len(self._rentalList):
            if self._rentalList[i].getClientId() == clientId:
                self._rentalList.pop(i)
                i = i - 2
            i = i +1

        #Delete the ClientsCounter
        del(self._rentedClientsCounter[clientId])

    def replaceClient(self, clientOld, clientNew):
        '''
        :param clientOld: Client object
        :param clientNew: Client object
        :return:
        '''

        #Change the ids in rentalList
        for i in range(len(self._rentalList)):
            if self._rentalList[i].getClientId() == clientOld.getClientId():
                self._rentalList[i].setClientId(clientNew.getClientId())

        #change the ids in rentedClientsCounter
        aux = self._rentedClientsCounter[clientOld.getClientId()]
        del(self._rentedClientsCounter[clientOld.getClientId()])
        self._rentedClientsCounter[clientNew.getClientId()] = aux

    def removeByMovieId(self, movieId):
        i = 0
        while i < len(self._rentalList):
            if self._rentalList[i].getMovieId() == movieId:
                self._rentalList.pop(i)
                i = i - 2
            i = i +1

        #Delete the MoviesCounter
        del(self._rentedMoviesCounter[movieId])

    def replaceMovie(self, movieOld, movieNew):

         for i in range(len(self._rentalList)):
            if self._rentalList[i].getMovieId() == movieOld.getMovieId():
                self._rentalList[i].setMovieId(movieOld.getMovieId())

         aux = self._rentedMoviesCounter[movieOld.getMovieId()]
         del(self._rentedMoviesCounter[movieOld.getMovieId()])

         self._rentedMoviesCounter[movieNew.getMovieId()] = aux




    def __str__(self):
        msg = "\nCLIENT ID | MOVIE ID | RENTED DATE | DUE DATE | RETURNED DATE\n"
        for crt in self._rentalList:
            msg = msg + str(crt.getClientId()) + ": " + str(crt.getMovieId()) + ", " + str(crt.getRentedDate()) + ", " + str(crt.getDueDate()) + ", " + str(crt.getReturnedDate())
            msg += "\n"
        return msg

    def __len__(self):
        return len(self._rentalList)