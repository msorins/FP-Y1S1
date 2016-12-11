__author__ = 'sorynsoo'

from datetime import datetime
from movieRental.Utils.utils import *

class Rental():
    idCount = 0;

    def __init__(self, clientId, movieId, rentedDate, dueDate, returnedDate):
        '''
        Instantiates the Rental Class
        :param clientId: integer
        :param movieId: integer
        :param rentedDate: Date Object
        :param dueDate:  Date Object
        :param returnedDate: Date Object
        '''
        self._utilsObject = Utils()

        self.setRentalId()
        self.setMovieId(movieId)
        self.setClientId(clientId)
        self.setRentedDate(rentedDate)
        self.setDueDate(dueDate)
        self.setReturnedDate(returnedDate)

    def setRentalId(self):
        '''
        Setter
        :return: sets automatially the rental id
        '''
        self._rentalId = Rental.idCount
        Rental.idCount = Rental.idCount + 1

    def getRentalId(self):
        '''
        Getter
        :return: the rental id
        '''
        return self._rentalId

    def setMovieId(self, movieId):
        '''
        Setter
        :param movieId: integer
        :return: sets the movie ID manually (override)
        '''
        self._movieId = movieId

    def getMovieId(self):
        '''
        Getter
        :return: gets the movie ID
        '''
        return self._movieId

    def setClientId(self, clientId):
        '''
        Setter
        :param clientId: string
        :return: sets the client id
        '''
        self._clientId = clientId

    def getClientId(self):
        '''
        Getter
        :return: the client id (the one who rented the movie)
        '''
        return self._clientId

    def setRentedDate(self, rentedDate):
        '''
        Setter
        :param rentedDate: Date Object
        :return: sets the RentedDate
        '''
        if rentedDate == "":
            self._returnedDate = ""
            return

        self._utilsObject.validateDateFormat(rentedDate)

        if type(rentedDate) == str:
            self._rentedDate = datetime.strptime(rentedDate, '%d.%m.%Y')
            return
        self._rentedDate = rentedDate

    def getRentedDate(self):
        '''
        Getter
        :return: the rented date
        '''
        return self._rentedDate

    def setDueDate(self, dueDate):
        '''
        Setter
        :param dueDate: Date Object
        :return:  sets the Due Date
        '''
        if dueDate == "":
            self._dueDate = ""
            return

        self._utilsObject.validateDateFormat(dueDate)

        if type(dueDate) == str:
            self._dueDate = datetime.strptime(dueDate, '%d.%m.%Y')
            return
        self._dueDate = dueDate

    def getDueDate(self):
        '''
        Getter
        :return: due date
        '''
        return self._dueDate

    def setReturnedDate(self, returnedDate):
        '''
        :param returnedDate: dateObject
        :return: sets the Returned Date
        '''
        if returnedDate == "":
            self._returnedDate = ""
            return

        self._utilsObject.validateDateFormat(returnedDate)

        if type(returnedDate) == str:
            self._returnedDate = datetime.strptime(returnedDate, '%d.%m.%Y')
            return
        self._returnedDate = returnedDate

    def getReturnedDate(self):
        '''
        Getter
        :return: returned Date
        '''
        return self._returnedDate
