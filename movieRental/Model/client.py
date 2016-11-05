__author__ = 'sorynsoo'

class Client:
    idCount = 0

    def __init__(self, name):
        self.setClientId()
        self.setName(name)

    def setClientId(self):
        self._clientId = Client.idCount
        Client.idCount = Client.idCount + 1

    def getClientId(self):
        return self._clientId

    def setName(self, name):
        self._name = name
    def getName(self):
        return self._name