__author__ = 'sorynsoo'
from movieRental.Model.rental import *
import operator
import copy

class RentalRepository():
    def __init__(self):
        '''
        Instantiate the Repo list
        '''
        self._rentalList = []
        self._rentedMoviesCounter = {}
        self._rentedClientsCounter = {}
        self._state = []

    def rentMovie(self, rental):
        '''
         Adds a rental request to the list
        :param rental: Rental Object
        '''
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
        '''
            Removes a rental request from the list
            :param rental: Rental Object
        '''
        ok = False
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getMovieId() == rental.getMovieId():
                crt.setReturnedDate(rental.getReturnedDate())
                ok = True

        if ok != True:
            raise RuntimeError("Operation could not have been executed")

    def canUserRent(self, rental):
        '''
        :param rental: Rental Object
        :return: True or False if the user can or can't rent movies
        '''
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getReturnedDate() != "" and crt.getReturnedDate() > crt.getDueDate():
                return False
        return True

    def mostRentedMovies(self):
        '''
        :return: A list containing the most Rented Movies
        '''
        rentedMovies = {}
        for crt in self._rentalList:
            try:
                rentedMovies[crt.getMovieId()] += 1;
            except Exception:
                rentedMovies[crt.getMovieId()] = 1;

        return sorted(rentedMovies.items(), key=operator.itemgetter(1), reverse = True)

    def mostActiveClients(self):
        '''
        :return: A list containing the most Active Clients
        '''
        clientsWhoRented = {}
        for crt in self._rentalList:
            try:
                clientsWhoRented[crt.getClientId()] += 1;
            except Exception:
                clientsWhoRented[crt.getClientId()] = 1;

        return sorted(clientsWhoRented.items(), key=operator.itemgetter(1), reverse = True)

    def rentalsAndMoviesCurrentlyRented(self):
        '''
        :return: A list containing the movies that are currently rented (and by what clients)
        '''
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
        '''
        :return: a list containing all the movies that are currently rented and unreturned
        '''
        rtrn = []
        for crt in self._rentalList:
            if crt.getReturnedDate() == "":
                continue

            if crt.getReturnedDate() > crt.getDueDate():
                    rtrn.append(crt)

        auxObj = sorted(rtrn, key = lambda x: ((x.getReturnedDate() - x.getDueDate()).days), reverse = True)

        return auxObj

    def incrementRentedMoviesCounter(self, rental):
        '''
        increments the Rented Movie Counter
        :param rental: Rental Object
        '''
        try:
            if rental.getMovieId() in self._rentedMoviesCounter.keys():
                self._rentedMoviesCounter[rental.getMovieId()] = self._rentedMoviesCounter[rental.getMovieId()] + 1
            else:
                self._rentedMoviesCounter[rental.getMovieId()] = 1
        except Exception:
            pass

    def getRentedMovieCounter(self, rental):
        '''
        :param rental: Rental Object
        :return: an integer
        '''
        try:
            return self._rentedMoviesCounter[rental.getMovieId()]
        except Exception:
            pass

    def incrementRentedClientsCounter(self, rental):
        '''
        Increments the Rented Clients Counter
        :param rental: Rental Object
        '''
        if rental.getClientId() in self._rentedClientsCounter.keys():
            self._rentedClientsCounter[rental.getClientId()] = self._rentedClientsCounter[rental.getClientId()] + 1
        else:
            self._rentedClientsCounter[rental.getClientId()] = 1

    def getRentedClientsCounter(self, rental):
        '''
        Getter for the rented Clients counter
        :param rental: Rental Object
        :return: an integer
        '''
        return self._rentedClientsCounter[rental.getClientId()]

    def removeByClientId(self, clientId):
        '''
        :param clientId: Integer
        '''
        i = 0
        while i < len(self._rentalList):
            if self._rentalList[i].getClientId() == clientId:
                self._rentalList.pop(i)
                i = i - 2
            i = i +1

        #Delete the ClientsCounter
        try:
            del(self._rentedClientsCounter[clientId])
        except Exception as e:
            pass

    def replaceClient(self, clientOld, clientNew):
        '''
        Replaces a client with another one
        :param clientOld: Client object
        :param clientNew: Client object
        '''

        #Change the ids in rentalList
        for i in range(len(self._rentalList)):
            if self._rentalList[i].getClientId() == clientOld.getClientId():
                self._rentalList[i].setClientId(clientNew.getClientId())

        #change the ids in rentedClientsCounter
        try:
            aux = self._rentedClientsCounter[clientOld.getClientId()]
            del(self._rentedClientsCounter[clientOld.getClientId()])
            self._rentedClientsCounter[clientNew.getClientId()] = aux
        except Exception as e:
            pass

    def removeByMovieId(self, movieId):
        '''
        :param movieId: Integer representing the movie id
        '''
        i = 0
        while i < len(self._rentalList):
            if self._rentalList[i].getMovieId() == movieId:
                self._rentalList.pop(i)
                i = i - 2
            i = i +1

        #Delete the MoviesCounter
        try:
            del(self._rentedMoviesCounter[movieId])
        except Exception:
            pass

    def replaceMovie(self, movieOld, movieNew):
         '''
         Replaces a movie with another one
         :param movieOld: movieObject
         :param movieNew: movieObject
         '''
         for i in range(len(self._rentalList)):
            if self._rentalList[i].getMovieId() == movieOld.getMovieId():
                self._rentalList[i].setMovieId(movieOld.getMovieId())

         try:
            aux = self._rentedMoviesCounter[movieOld.getMovieId()]
            del(self._rentedMoviesCounter[movieOld.getMovieId()])
            self._rentedMoviesCounter[movieNew.getMovieId()] = aux
         except Exception:
             pass

    def __str__(self):
        '''
        :return: a nicely formatted string ready to be printed
        '''
        msg = "\nCLIENT ID | MOVIE ID | RENTED DATE | DUE DATE | RETURNED DATE\n"
        for crt in self._rentalList:
            msg = msg + str(crt.getClientId()) + ": " + str(crt.getMovieId()) + ", " + str(crt.getRentedDate()) + ", " + str(crt.getDueDate()) + ", " + str(crt.getReturnedDate())
            msg += "\n"
        return msg

    def __len__(self):
        '''
        :return: the number of elements in the rentalList
        '''
        return len(self._rentalList)
