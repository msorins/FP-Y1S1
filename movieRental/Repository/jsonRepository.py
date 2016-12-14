import json

from movieRental.Model.client import *
from movieRental.Model.movie import *
from movieRental.Model.rental import *
import inspect

class JsonRepository():
    def __init__(self):
        pass

    def save(self, obj, type, path):
        '''
        :param obj: the object which will be written
        :param path: the path of the file
        '''
        fileObj = {}
        for crt in obj:
            if type == "Client":
                fileObj[crt.getClientId()] = {"name": str(crt.getName())}
            if type == "Movie":
                fileObj[crt.getMovieId()] = {"title": str(crt.getTitle()), "description": str(crt.getDescription()), "genre": str(crt.getGenre())}
            if type == "Rental":
                rentedDate = str(crt.getRentedDate()).replace(" 00:00:00", "").split("-")
                rentedDate = rentedDate[2] + "." + rentedDate[1] + "." + rentedDate[0]

                dueDate = str(crt.getDueDate()).replace(" 00:00:00", "").split("-")
                dueDate = dueDate[2] + "." + dueDate[1] + "." + dueDate[0]

                returnedDate = ""
                if (crt.getReturnedDate() != ""):
                    returnedDate = str(crt.getReturnedDate()).replace(" 00:00:00", "").split("-")
                    returnedDate = returnedDate[2] + "." + returnedDate[1] + "." + returnedDate[0]

                fileObj[crt.getRentalId()] = {"movieId": str(crt.getMovieId()) , "clientId": str(crt.getClientId()), "rentedDate": rentedDate, "dueDate": dueDate, "returnedDate": returnedDate }
        open(path+".json", 'w').write(json.dumps(fileObj))

    def load(self, type, path):
        path = path + ".json"
        objectsList = []
        try:
            with open(path) as file:
                for line in file:
                    jsonObj = json.loads(line.strip("'"))

                    for key in jsonObj:
                        if type == "Client":
                            crtObj = Client(jsonObj[key]["name"])
                            crtObj.setManuallyClientId(int(key))
                        if type == "Movie":
                            crtObj = Movie(jsonObj[key]["title"], jsonObj[key]["description"], jsonObj[key]["genre"])
                            crtObj.setManuallyMovieId(int(key))
                        if type == "Rental":
                            crtObj = Rental(jsonObj[key]["movieId"], jsonObj[key]["clientId"], jsonObj[key]["rentedDate"], jsonObj[key]["dueDate"], jsonObj[key]["returnedDate"])
                            crtObj.setManuallyRentalId(int(key))

                        objectsList.append(crtObj)

        except IOError as e:
            print(e)

        return objectsList