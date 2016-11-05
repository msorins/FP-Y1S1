__author__ = 'sorynsoo'

from datetime import datetime
from movieRental.Utils.utils import *

class Rental():
    idCount = 0;

    def __init__(self, clientId, movieId, rentedDate, dueDate, returnedDate):
        self._utilsObject = Utils()

        self.setRentalId()
        self.setMovieId(movieId)
        self.setClientId(clientId)
        self.setRentedDate(rentedDate)
        self.setDueDate(dueDate)
        self.setReturnedDate(returnedDate)

    def setRentalId(self):
        self._rentalId = Rental.idCount
        Rental.idCount = Rental.idCount + 1

    def getRentalId(self):
        return self._rentalId

    def setMovieId(self, movieId):
        self._movieId = movieId

    def getMovieId(self):
        return self._movieId

    def setClientId(self, clientId):
        self._clientId = clientId

    def getClientId(self):
        return self._clientId

    def setRentedDate(self, rentedDate):
        if rentedDate == "":
            self._returnedDate = ""
            return

        self._utilsObject.validateDateFormat(rentedDate)

        if type(rentedDate) == str:
            self._rentedDate = datetime.strptime(rentedDate, '%d.%m.%Y')
            return
        self._rentedDate = rentedDate

    def getRentedDate(self):
        return self._rentedDate

    def setDueDate(self, dueDate):
        if dueDate == "":
            self._dueDate = ""
            return

        self._utilsObject.validateDateFormat(dueDate)

        if type(dueDate) == str:
            self._dueDate = datetime.strptime(dueDate, '%d.%m.%Y')
            return
        self._dueDate = dueDate

    def getDueDate(self):
        return self._dueDate

    def setReturnedDate(self, returnedDate):
        if returnedDate == "":
            self._returnedDate = ""
            return

        self._utilsObject.validateDateFormat(returnedDate)

        if type(returnedDate) == str:
            self._returnedDate = datetime.strptime(returnedDate, '%d.%m.%Y')
            return
        self._returnedDate = returnedDate

    def getReturnedDate(self):
        return self._returnedDate
