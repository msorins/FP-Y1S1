__author__ = 'sorynsoo'

from movieRental.Model.movie import *
from movieRental.Repository.movieRepository import *

from movieRental.Model.client import *
from movieRental.Repository.clientRepository import *

from movieRental.Model.rental import *
from movieRental.Repository.rentalRepository import *

from movieRental.View.commandUI import *

from movieRental.Tests.tests import *

from movieRental.Controller.mainController import *

from movieRental.PopulateDB.PopulateDB import *

def initFunction():

    mainControllerObj = MainController()
    populateDbObj = PopulateDB(mainControllerObj._movieRepository, mainControllerObj._clientRepository, mainControllerObj._rentalRepository)
    mainControllerObj.saveState()

    while 1:
        try:
            uiObj = CommandUI(mainControllerObj)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    initFunction()

