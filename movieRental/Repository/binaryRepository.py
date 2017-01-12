
from movieRental.Model.client import *
from movieRental.Model.movie import *
from movieRental.Model.rental import *
import inspect
import pickle

from movieRental.iterableDataStruct.IterableDataStruct import IterableDataStruct


class BinaryRepository():
    def __init__(self):
        pass

    def save(self, obj, type, path):
        '''
        :param obj: the object which will be written
        :param path: the path of the file
        '''
        try:
            with open(path + ".pickle", "wb") as f:
                if type == "Client":
                    pickle.dump(obj._clientList, f)
                elif type == "Movie":
                    pickle.dump(obj._movieList, f)
                elif type == "Rental":
                    pickle.dump(obj._rentalList, f)

        except IOError as e:
            print(e)

    def load(self, type, path):
        returnedObj = IterableDataStruct()
        path = path + ".pickle"
        try:
            with open(path, "rb") as file:
                returnedObj = pickle.load(file)

        except IOError as e:
            print(e)

        for i in range(len(returnedObj)):
            if type == "Client":
                Client("ABC")
            elif type == "Movie":
                Movie("ABC", "ABC", "ABC")
            elif type == "Rental":
                Rental("0", "0", "11.11.2016", "11.11.2016", "11.11.2016")
        return returnedObj