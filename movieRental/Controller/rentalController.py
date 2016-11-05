__author__ = 'sorynsoo'
from movieRental.Model.rental import *

class RentalController():
    def __init__(self):
        self._rentalList = []

    def rentMovie(self, rental):
        if not self.canUserRent(rental):
            raise RuntimeError("User cannot rent movie due to the fact that is untrustworty")
            return

        if(type(rental) == Rental):
            self._rentalList.append(rental)
            print(str(rental.getClientId()) + " request added to the rental log")
        else:
            raise TypeError("Invalid rental format")

    def returnMovie(self, rental):
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getMovieId() == rental.getMovieId():
                crt.setReturnedDate(rental.getReturnedDate())


    def canUserRent(self, rental):
        for crt in self._rentalList:
            if crt.getClientId() == rental.getClientId() and crt.getReturnedDate() != "" and crt.getReturnedDate() > crt.getDueDate():
                return False
        return True

    def __str__(self):
        msg = "\nCLIENT ID | MOVIE ID | RENTED DATE | DUE DATE | RETURNED DATE\n"
        for crt in self._rentalList:
            msg = msg + str(crt.getClientId()) + ": " + str(crt.getMovieId()) + ", " + str(crt.getRentedDate()) + ", " + str(crt.getDueDate()) + ", " + str(crt.getReturnedDate())
            msg += "\n"
        return msg

    def __len__(self):
        return len(self._rentalList)
