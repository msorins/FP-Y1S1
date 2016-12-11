__author__ = 'sorynsoo'

from movieRental.Utils.utils import *

class Client:
    idCount = 0

    def __init__(self, name):
        '''
        :param name: a string reffering to the name of the client
        '''
        self._utilsObject = Utils()
        
        self.setClientId()
        self.setName(name)

    def setClientId(self):
        '''
        :return: sets the client id automatically
        '''
        self._clientId = Client.idCount
        Client.idCount = Client.idCount + 1

    def setManuallyClientId(self, id):
        '''
            :return: sets the client id manually (override)
        '''
        self._clientId = id;

    def getClientId(self):
        '''
        :return: client's id
        '''
        return self._clientId

    def setName(self, name):
        '''
        Setter
        :param name: a string containing the name of the current client
        :return: sets _name
        '''
        self._utilsObject.nonEmptyAndMoreThanThree(name)
        self._name = name

    def getName(self):
        '''
        Getter
        :return: client's name
        '''
        return self._name