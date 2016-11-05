__author__ = 'sorynsoo'


from movieRental.Controller.movieController import *
from movieRental.Controller.clientController import *
from movieRental.Controller.rentalController import *

class CommandUI:
    def __init__(self, movieController, clientController, rentalController):
        self._movieController = movieController
        self._clientController = clientController
        self._rentalController = rentalController

        self._menu = [
            {"id" : 1, "msg": "client commands", "final" : False, "next": [
                {"id" : 1, "msg": "add client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client1", "method" : self._clientController.addClient}
                ]},
                {"id" : 2, "msg": "remove client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client1", "method" : self._clientController.removeClient}
                ]},
                {"id" : 3, "msg": "replace client", "final": False, "next" : [
                    { "msg" : "<oldName> <newName>", "final" : True, "type": "client2", "method" : self._clientController.replaceClient}
                ]},
                {"id" : 4, "msg": "print", "final" : True, "obj": self._clientController}
            ]},
            {"id" : 2, "msg": "movie commands", "final" : False, "next": [
                {"id" : 1, "msg": "add movie", "final" : False, "next" : [
                    { "msg" : "<title> <description> <genre>", "final" : True, "type": "movie1", "method" : self._movieController.addMovie}
                ]},
                {"id" : 2, "msg": "remove movie", "final" : False, "next" : [
                    { "msg" : "<title>", "final" : True, "type": "movie2", "method" : self._movieController.removeMovie}
                ]},
                {"id" : 3, "msg": "replace movie", "final": False, "next" : [
                    { "msg" : "<replacedTitle> <newTitle> <newDescription> <newGenre>", "final" : True, "type": "movie3", "method" : self._movieController.replaceMovie}
                ]},
                {"id" : 4, "msg": "print", "final" : True, "obj": self._movieController}
            ]},
            {"id" : 3, "msg": "rental commands", "next": [
                {"id" : 1, "msg": "rent movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <rentedDate> <dueDate>", "final" : True, "type": "rental1", "method" : self._rentalController.rentMovie}
                ]},
                {"id" : 2, "msg": "return movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <returnedDate>", "final" : True, "type": "rental2", "method" : self._rentalController.returnMovie}
                ]},
                {"id" : 3, "msg": "print", "final" : True, "obj": self._rentalController}
            ]},
            {"id" : "9", "msg": "exit"}
        ]

        self.showMenu(self._menu)


    def showMenu(self, menu):
        if len(menu) > 1:
            for crt in menu:
                print(str(crt["id"]) + " : " + str(crt["msg"]))

            inputNumber = int(input("Command number: "))

            if inputNumber == 9:
                self.showMenu(self._menu)
                return
            if inputNumber == len(menu):
                print(menu[inputNumber-1]["obj"])
                self.showMenu(self._menu)
                return

            self.showMenu(menu[inputNumber - 1]["next"])
        else:
            print(str(menu[0]["msg"]))

            if menu[0]["type"] == "client1":
                menu[0]["method"](Client(input("Name: ")))
            if menu[0]["type"] == "client2":
                menu[0]["method"](Client(input("oldName: ")), Client(input("newName: ")))
            if menu[0]["type"] == "movie1":
                menu[0]["method"](Movie(input("Title: "), input("Description: "), input("Genre: ")))
            if menu[0]["type"] == "movie2":
                menu[0]["method"](Movie(input("Title: "), "", ""))
            if menu[0]["type"] == "movie3":
                menu[0]["method"](Movie(input("Replaced title: "), "", ""), Movie(input("Title: "), input("Description: "), input("Genre: ")))
            if menu[0]["type"] == "rental1":
                menu[0]["method"](Rental(self._clientController.getClientIdByName(input("Client name: ")), self._movieController.getMovieIdByName(input("Movie name: ")), input("Rented date: "), input("Due date: "), ""))
            if menu[0]["type"] == "rental2":
                menu[0]["method"](Rental(self._clientController.getClientIdByName(input("Client name: ")), self._movieController.getMovieIdByName(input("Movie name: ")), "", "", str(input("Returned date: "))))


            self.showMenu(self._menu)





