
from movieRental.Model.client import *
from movieRental.Model.movie import *
from movieRental.Model.rental import *
import inspect

class FileRepository():
    def __init__(self):
        pass

    def save(self, obj, type, path):
        '''
        :param obj: the object which will be written
        :param path: the path of the file
        '''
        FileStr = ""
        for crt in obj:
            if type == "Client":
                FileStr += str(crt.getClientId()) + "<;>" + str(crt.getName())
            if type == "Movie":
                FileStr += str(crt.getMovieId()) + "<;>" + str(crt.getTitle()) + "<;>" + str(crt.getDescription()) + "<;>" + str(crt.getGenre())
            if type== "Rental":
                rentedDate = str(crt.getRentedDate()).replace(" 00:00:00", "").split("-")
                rentedDate = rentedDate[2] + "." + rentedDate[1] + "." + rentedDate[0]

                dueDate = str(crt.getDueDate()).replace(" 00:00:00", "").split("-")
                dueDate = dueDate[2] + "." + dueDate[1] + "." + dueDate[0]

                returnedDate = ""
                if(crt.getReturnedDate() != ""):
                    returnedDate = str(crt.getReturnedDate()).replace(" 00:00:00", "").split("-")
                    returnedDate = returnedDate[2] + "." + returnedDate[1] + "." + returnedDate[0]


                FileStr += str(crt.getRentalId()) + "<;>" + str(crt.getMovieId()) + "<;>" + str(crt.getClientId()) + "<;>" + rentedDate + "<;>" + dueDate + "<;>" + returnedDate

            FileStr += "\n"

        open(path, 'w').write(FileStr)


    def load(self, type, path):
        objectsList = []
        try:
            with open(path) as file:
                for line in file:
                    line = line.split("<;>")
                    if type == "Client":
                        crtObj = Client(line[1].rstrip('\n'))
                        crtObj.setManuallyClientId(int(line[0]))
                    if type == "Movie":
                        crtObj = Movie(line[1], line[2], line[3].rstrip('\n'))
                        crtObj.setManuallyMovieId(int(line[0]))
                    if type == "Rental":
                        crtObj = Rental(line[1], line[2], line[3], line[4], line[5].rstrip('\n'))
                        crtObj.setManuallyRentalId(int(line[0]))

                    objectsList.append(crtObj)
        except IOError as e:
            print(e)

        return objectsList