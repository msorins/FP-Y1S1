__author__ = 'sorynsoo'

from movieRental.Model.movie import *
from movieRental.Controller.movieController import *

from movieRental.Model.client import *
from movieRental.Controller.clientController import *

from movieRental.Model.rental import *
from movieRental.Controller.rentalController import *

from movieRental.View.commandUI import *

from movieRental.Tests.tests import *

def initFunction():

    movieControllerObj = MovieController()
    clientControllerObj = ClientController()
    rentalControllerObj = RentalController()
    Tests(movieControllerObj, clientControllerObj, rentalControllerObj)

    while 1:
        try:
            uiObj = CommandUI(movieControllerObj, clientControllerObj, rentalControllerObj)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    initFunction()

