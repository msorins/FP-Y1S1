__author__ = 'sorynsoo'


from movieRental.Model.client import *

class ClientController():
    def __init__(self):
        self._clientList = []

    def addClient(self, client):
        if self.findClient(client) != -1:
            raise RuntimeError("There already exists a user with this name")
        self._clientList.append(client)
        if(type(client) == Client):
            print(client.getName() + " added to the client list")
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

    def findClient(self, client):
        for i in range(len(self._clientList)):
            if self._clientList[i].getName() == client.getName():
                return i
        return -1

    def getClientIdByName(self, name):
        for crt in self._clientList:
            if crt.getName() == name:
                return crt.getClientId()

        raise RuntimeError("User not found")

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