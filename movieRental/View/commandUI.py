__author__ = 'sorynsoo'

from movieRental.Controller.movieController import *
from movieRental.Controller.clientController import *
from movieRental.Controller.rentalController import *
from movieRental.Utils.utils import *

class CommandUI:
    def __init__(self, movieController, clientController, rentalController):
        self._utilsObject = Utils()
        self._movieController = movieController
        self._clientController = clientController
        self._rentalController = rentalController

        self._menu = [
            {"id" : 1, "msg": "Client commands", "final" : False, "next": [
                {"id" : 1, "msg": "Add client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client1", "method" : self._clientController.addClient}
                ]},
                {"id" : 2, "msg": "Remove client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client1", "method" : self._clientController.removeClient}
                ]},
                {"id" : 3, "msg": "Replace client", "final": False, "next" : [
                    { "msg" : "<oldName> <newName>", "final" : True, "type": "client2", "method" : self._clientController.replaceClient}
                ]},
                {"id" : 4, "msg": "Find client", "final": False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client3", "method" : self._clientController.findClients}
                ]},
                {"id" : 5, "msg": "Undo", "final": False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "undo", "method" : self._clientController.restoreState}
                ]},
                {"id" : 6, "msg": "Print", "final" : True, "obj": self._clientController}
            ]},
            {"id" : 2, "msg": "Movie commands", "final" : False, "next": [
                {"id" : 1, "msg": "Add movie", "final" : False, "next" : [
                    { "msg" : "<title> <description> <genre>", "final" : True, "type": "movie1", "method" : self._movieController.addMovie}
                ]},
                {"id" : 2, "msg": "Remove movie", "final" : False, "next" : [
                    { "msg" : "<title>", "final" : True, "type": "movie2", "method" : self._movieController.removeMovie}
                ]},
                {"id" : 3, "msg": "Replace movie", "final": False, "next" : [
                    { "msg" : "<replacedTitle> <newTitle> <newDescription> <newGenre>", "final" : True, "type": "movie3", "method" : self._movieController.replaceMovie}
                ]},
                {"id" : 4, "msg": "Find movie", "final" : False, "next" : [
                    { "msg" : "<title> <description> <genre>", "final" : True, "type": "movie4", "method" : self._movieController.findMovies}
                ]},
                {"id" : 5, "msg": "Undo", "final": False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "undo", "method" : self._movieController.restoreState}
                ]},
                {"id" : 6, "msg": "Print", "final" : True, "obj": self._movieController}
            ]},
            {"id" : 3, "msg": "Rental commands", "next": [
                {"id" : 1, "msg": "Rent movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <rentedDate> <dueDate>", "final" : True, "type": "rental1", "method" : self._rentalController.rentMovie}
                ]},
                {"id" : 2, "msg": "Return movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <returnedDate>", "final" : True, "type": "rental2", "method" : self._rentalController.returnMovie}
                ]},
                {"id" : 3, "msg": "Undo", "final": False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "undo", "method" : self._rentalController.restoreState}
                ]},
                {"id" : 4, "msg": "Print", "final" : True, "obj": self._rentalController}
            ]},
            {"id" : 4, "msg": "Stats commands", "next": [
                {"id" : 1, "msg": "Most rented movies", "final" : True, "next" : [
                    {"type": "stats1", "msg": "Printing most rented movies:", "final" : True, "method": self._rentalController.mostRentedMovies}
                ]},
                {"id" : 2, "msg": "Most active clients", "final" : True, "next" : [
                    {"type": "stats2", "msg": "Printing most active clients:", "final" : True, "method": self._rentalController.mostActiveClients}
                ]},
                {"id" : 3, "msg": "All current rentals & all currently rented movies", "final" : True, "next" : [
                    {"type": "stats3", "msg": "Printing your stats:", "final" : True, "method": self._rentalController.rentalsAndMoviesCurrentlyRented}
                ]},
                {"id" : 4, "msg": "Late rentals sorted by the delay", "final" : True, "next" : [
                    {"type": "stats4", "msg": "Printing your stats:", "final" : True, "method": self._rentalController.currentlyRentedUnreturnedMovies}
                ]}
            ]}
        ]

        self.showMenu(self._menu)


    def showMenu(self, menu):
        if len(menu) > 1:
            print("\n---MENU----")
            for crt in menu:
                print(str(crt["id"]) + " : " + str(crt["msg"]))

            inputNumber = input("Command number: ")
            self._utilsObject.validateCommandNumber(menu, inputNumber)
            inputNumber = int(inputNumber)

            if inputNumber == 9:
                self.showMenu(self._menu)
                return
            if inputNumber == len(menu) and menu[inputNumber-1]["msg"] == "Print":
                print(menu[inputNumber-1]["obj"])
                self.showMenu(self._menu)
                return

            self.showMenu(menu[inputNumber - 1]["next"])
        else:
            print("\n---MENU----")
            print(str(menu[0]["msg"]))

            if menu[0]["type"] == "client1":
                menu[0]["method"](Client(input("Name: ")))
            if menu[0]["type"] == "client2":
                menu[0]["method"](Client(input("oldName: ")), Client(input("newName: ")))
            if menu[0]["type"] == "client3":
                print(menu[0]["method"](Client(input("Name: "))))
            if menu[0]["type"] == "movie1":
                menu[0]["method"](Movie(input("Title: "), input("Description: "), input("Genre: ")))
            if menu[0]["type"] == "movie2":
                menu[0]["method"](Movie(input("Title: "), "", ""))
            if menu[0]["type"] == "movie3":
                menu[0]["method"](Movie(input("Replaced title: "), "", ""), Movie(input("Title: "), input("Description: "), input("Genre: ")))
            if menu[0]["type"] == "movie4":
                print(menu[0]["method"](Movie(Utils.bypassValidation(input("Title: ")), Utils.bypassValidation(input("Description: ")), Utils.bypassValidation(input("Genre: ")))))
            if menu[0]["type"] == "rental1":
                menu[0]["method"](Rental(self._clientController.getClientIdByName(input("Client name: ")), self._movieController.getMovieIdByName(input("Movie name: ")), input("Rented date: "), input("Due date: "), ""))
            if menu[0]["type"] == "rental2":
                menu[0]["method"](Rental(self._clientController.getClientIdByName(input("Client name: ")), self._movieController.getMovieIdByName(input("Movie name: ")), "", "", str(input("Returned date: "))))
            if menu[0]["type"] == "stats1":
                print(self.mostRentedMoviesUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats2":
                print(self.mostActiveClientsUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats3":
                print(self.rentalsAndMoviesCurrentlyRentedUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats4":
                print(self.currentlyRentedUnreturnedMoviesUI(menu[0]["method"]()))
            if menu[0]["type"] == "undo":
                 menu[0]["method"]()

            self.showMenu(self._menu)

    def validateCommandNumber(self, menu, command):
        rgx = re.compile(r"^[\d]+$")
        if not rgx.match(command):
            raise RuntimeError("Wrong command")
        if ( int(command) > len(menu) and int(command) !=9 ) or  int(command) < 0:
            raise RuntimeError("Invalid number")

    def mostRentedMoviesUI(self, obj):
        out = "\n\nMovie Title: Nr of times rented\n"

        for crt in obj:
            out = out + self._movieController.getMovieById(crt[0]).getTitle() + ": " + str(crt[1]) + "\n"

        return out

    def mostActiveClientsUI(self, obj):
        out = "\n\nName: Nr of movies rented\n"

        for crt in obj:
            out = out + self._clientController.getClientById(crt[0]).getName() + ": " + str(crt[1]) + "\n"

        return out

    def rentalsAndMoviesCurrentlyRentedUI(self, obj):
        out = "\n\nCurrent rentals:\n"
        out = out + "ID: ClientName\n"
        for clientId in obj.keys():
            out = out + str(clientId) + ": " + self._clientController.getClientById(clientId).getName() + "\n"
            out = out + "  ID: Movie Title\n"
            for movieId in obj[clientId]:
                out = out + "  " + str(movieId) + ": " + self._movieController.getMovieById(movieId).getTitle()  + "\n"
            out = out + "\n"

        return out

    def currentlyRentedUnreturnedMoviesUI(self, obj):
        out = "\n\nID: Movie Title, Nr. of days passed\n"

        for crt in obj:
            out = out + str(crt.getMovieId()) +": " + self._movieController.getMovieById(crt.getMovieId()).getTitle() + ", " + str((crt.getReturnedDate() - crt.getDueDate()).days) + " days passed\n"

        return out