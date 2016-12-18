from movieRental.Model.client import *
from movieRental.Model.movie import *
from movieRental.Model.rental import *
import inspect
import pickle
import sqlite3

class SqlRepository():
    def __init__(self):
        self._sqlConnection = sqlite3.connect('sqlMovieRental.db')

        self._sqlConnection.execute("CREATE TABLE IF NOT EXISTS Client(`id` int(11) NOT NULL, `name` text NOT NULL);")
        self._sqlConnection.execute("CREATE TABLE IF NOT EXISTS Movie ( `movieId` INT NOT NULL , `title` TEXT NOT NULL , `description` TEXT NOT NULL , `genre` TEXT NOT NULL );")
        self._sqlConnection.execute("CREATE TABLE IF NOT EXISTS Rental( `rentalId` INT NOT NULL , `movieId` INT NOT NULL , `clientId` INT NOT NULL , `rentedDate` TEXT NOT NULL , `dueDate` TEXT NOT NULL , `returnedDate` TEXT NOT NULL );")

        self._sqlConnection.commit()
        self._sqlConnection.close()

    def save(self, obj, type, path):
        '''
        :param obj: the object which will be written
        :param path: the path of the file
        '''
        self._sqlConnection = sqlite3.connect('sqlMovieRental.db')

        for crt in obj:
            if type == "Client":
                self._sqlConnection.execute("INSERT INTO `Client` (`id`, `name`) VALUES (?, ?)", (str(crt.getClientId()), str(crt.getName())))
                self._sqlConnection.commit()

            if type == "Movie":
                self._sqlConnection.execute("INSERT INTO `Movie` (`movieId`, `title`, `description`, `genre`) VALUES (?, ?, ?, ?)", (str(crt.getMovieId()), str(crt.getTitle()), str(crt.getDescription()), str(crt.getGenre())))
                self._sqlConnection.commit()

            if type== "Rental":
                rentedDate = str(crt.getRentedDate()).replace(" 00:00:00", "").split("-")
                rentedDate = rentedDate[2] + "." + rentedDate[1] + "." + rentedDate[0]

                dueDate = str(crt.getDueDate()).replace(" 00:00:00", "").split("-")
                dueDate = dueDate[2] + "." + dueDate[1] + "." + dueDate[0]

                returnedDate = ""
                if(crt.getReturnedDate() != ""):
                    returnedDate = str(crt.getReturnedDate()).replace(" 00:00:00", "").split("-")
                    returnedDate = returnedDate[2] + "." + returnedDate[1] + "." + returnedDate[0]

                self._sqlConnection.execute("INSERT INTO `Rental` (`rentalId`, `movieId`, `clientId`, `rentedDate`, `dueDate`, `returnedDate`) VALUES (?, ?, ?, ?, ?, ?)", ( str(crt.getRentalId()), str(crt.getMovieId()), str(crt.getClientId()), rentedDate, dueDate, returnedDate ))
                self._sqlConnection.commit()

        self._sqlConnection.close()

    def load(self, type, path):
        self._sqlConnection = sqlite3.connect('sqlMovieRental.db')

        objectsList = []
        if type == "Client":
            cursor = self._sqlConnection.execute("SELECT * FROM `Client`")
            for row in cursor:
                crtObj = Client(row[1])
                crtObj.setManuallyClientId(int(row[0]))

                objectsList.append(crtObj)

        if type == "Movie":
            cursor = self._sqlConnection.execute("SELECT * FROM `Movie`")
            for row in cursor:
                crtObj = Movie(row[1], row[2], row[3])
                crtObj.setManuallyMovieId(int(row[0]))

                objectsList.append(crtObj)

        if type == "Rental":
            cursor = self._sqlConnection.execute("SELECT * FROM `Rental`")
            for row in cursor:
                crtObj = Rental(row[1], row[2], row[3], row[4], row[5])
                crtObj.setManuallyRentalId(int(row[0]))

                objectsList.append(crtObj)

        self._sqlConnection.close()
        return objectsList
