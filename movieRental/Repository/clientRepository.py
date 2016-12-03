__author__ = 'sorynsoo'


from movieRental.Model.client import *
from movieRental.Utils.utils import *
import copy

class ClientRepository():
    def __init__(self):
        self._clientList = []

    def addClient(self, client):
        if self.findClient(client) != -1:
            raise RuntimeError("There already exists a user with this name")

        if(type(client) == Client):
            #print(client.getName() + " added to the client list")
            self._clientList.append(client)
        else:
            raise TypeError("Invalid client format")

    def removeClient(self, client):
        searchedIndex = self.findClient(client)
        if searchedIndex == -1:
            raise RuntimeError("Client does not exist, can't remove")

        self._clientList.pop(searchedIndex)

    def replaceClient(self, clientOld, clientNew):
        searchedIndex = self.findClient(clientOld)
        if searchedIndex == -1:
            raise RuntimeError("Client does not exist")

        self._clientList[searchedIndex] = clientNew

    def findClients(self, client):
      result = ClientRepository()

      #Search by case-insensitive name + partial names
      for i in range(len(self._clientList)):
          if Utils().findPartial(self._clientList[i].getName(), client.getName()):
              result.addClient(self._clientList[i])

      return result

    def findClient(self, client):
        for i in range(len(self._clientList)):
            if self._clientList[i].getName() == client.getName():
                return i
        return -1

    def getClientIdByName(self, name):
        for crt in self._clientList:
            if crt.getName() == name:
                return crt.getClientId()

        raise RuntimeError("Client not found")

    def getClientById(self, id):
        for crt in self._clientList:
            if crt.getClientId() == id:
                return crt

        raise RuntimeError("Client not found")

    def __iter__(self):
        for elem in self._clientList:
            yield elem

    def __str__(self):
        msg = "\nID | NAME\n"
        for crt in self._clientList:
            msg += str(crt.getClientId()) + " : " + str(crt.getName())
            msg += "\n"
        return msg

    def __len__(self):
        return len(self._clientList)