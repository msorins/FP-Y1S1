__author__ = 'sorynsoo'

from movieRental.Model.movie import *
from movieRental.Controller.movieController import *

from movieRental.Model.client import *
from movieRental.Controller.clientController import *

from movieRental.Model.rental import *
from movieRental.Controller.rentalController import *

from movieRental.View.commandUI import *


def initFunction():

    movieControllerObj = MovieController()
    clientControllerObj = ClientController()
    rentalControllerObj = RentalController()

    clientControllerObj.addClient(Client("so"))
    clientControllerObj.addClient(Client("lupi"))
    movieControllerObj.addMovie(Movie("supernatural", "cel mai tare", "horror"))
    movieControllerObj.addMovie(Movie("superman", "al doilea cel mai tare", "sci-fi"))
    rentalControllerObj.rentMovie(Rental(clientControllerObj.getClientIdByName("so"), movieControllerObj.getMovieIdByName("supernatural"),"1.11.2016","10.11.2016", ""))
    rentalControllerObj.rentMovie(Rental(clientControllerObj.getClientIdByName("lupi"), movieControllerObj.getMovieIdByName("supernatural"),"15.11.2016","20.11.2016", ""))

    while 1:
        try:
            uiObj = CommandUI(movieControllerObj, clientControllerObj, rentalControllerObj)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    initFunction()

