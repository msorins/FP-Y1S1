__author__ = 'sorynsoo'

from movieRental.Utils.utils import *

class Client:
    idCount = 0

    def __init__(self, name):
        self._utilsObject = Utils()
        
        self.setClientId()
        self.setName(name)

    def setClientId(self):
        self._clientId = Client.idCount
        Client.idCount = Client.idCount + 1

    def setManuallyClientId(self, id):
        self._clientId = id;

    def getClientId(self):
        return self._clientId

    def setName(self, name):
        self._utilsObject.nonEmptyAndMoreThanThree(name)
        self._name = name

    def getName(self):
        return self._name