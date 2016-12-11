__author__ = 'sorynsoo'


from movieRental.Model.client import *
from movieRental.Utils.utils import *
import copy

class ClientRepository():
    def __init__(self):
        '''
        Instantiate the class with an empty lists of clients
        '''
        self._clientList = []

    def addClient(self, client):
        '''
        Adds a client
        :param client: Client Object
        '''
        if self.findClient(client) != -1:
            raise RuntimeError("There already exists a user with this name")

        if(type(client) == Client):
            #print(client.getName() + " added to the client list")
            self._clientList.append(client)
        else:
            raise TypeError("Invalid client format")

    def removeClient(self, client):
        '''
        Removes a client
        :param client: Client Object
        '''
        searchedIndex = self.findClient(client)
        if searchedIndex == -1:
            raise RuntimeError("Client does not exist, can't remove")

        self._clientList.pop(searchedIndex)

    def replaceClient(self, clientOld, clientNew):
        '''
        Replaces a client with a new client
        :param clientOld: Client Object
        :param clientNew: Client Object
        '''
        searchedIndex = self.findClient(clientOld)
        if searchedIndex == -1:
            raise RuntimeError("Client does not exist")

        self._clientList[searchedIndex] = clientNew

    def findClients(self, client):
      '''
      Finds multiple clients by multiple attributes
      :param client: Client Object
      :return: a list of clients
      '''
      result = ClientRepository()

      #Search by case-insensitive name + partial names
      for i in range(len(self._clientList)):
          if Utils().findPartial(self._clientList[i].getName(), client.getName()):
              result.addClient(self._clientList[i])

      return result

    def findClient(self, client):
        '''
        Finds just one client
        :param client:  Client Object
        :return: an integer representing the found client id or -1 if it is not found
        '''
        for i in range(len(self._clientList)):
            if self._clientList[i].getName() == client.getName():
                return i
        return -1

    def getClientIdByName(self, name):
        '''
        :param name: string
        :return: Client Object or excepton is raised if it is not found
        '''
        for crt in self._clientList:
            if crt.getName() == name:
                return crt.getClientId()

        raise RuntimeError("Client not found")

    def getClientById(self, id):
        '''
        :param id: integer
        :return: Client Object that was found
        '''
        for crt in self._clientList:
            if crt.getClientId() == id:
                return crt

        raise RuntimeError("Client not found")

    def __iter__(self):
        for elem in self._clientList:
            yield elem

    def __str__(self):
        '''
        Prints all the repo
        :return: a nicely formatted string
        '''
        msg = "\nID | NAME\n"
        for crt in self._clientList:
            msg += str(crt.getClientId()) + " : " + str(crt.getName())
            msg += "\n"
        return msg

    def __len__(self):
        '''
        :return: the number of clients in the Repo
        '''
        return len(self._clientList)