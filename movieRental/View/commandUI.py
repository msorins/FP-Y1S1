__author__ = 'sorynsoo'

from movieRental.Repository.movieRepository import *
from movieRental.Repository.clientRepository import *
from movieRental.Repository.rentalRepository import *
from movieRental.Utils.utils import *

class CommandUI:
    def __init__(self, mainController):
        self._utilsObject = Utils()
        self._mainController = mainController

        self._menu = [
            {"id" : 1, "msg": "Client commands", "final" : False, "next": [
                {"id" : 1, "msg": "Add client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client0", "method" : self._mainController._clientRepository.addClient}
                ]},
                {"id" : 2, "msg": "Remove client", "final" : False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client1", "method" : self._mainController.removeClient}
                ]},
                {"id" : 3, "msg": "Replace client", "final": False, "next" : [
                    { "msg" : "<oldName> <newName>", "final" : True, "type": "client2", "method" : self._mainController.replaceClient}
                ]},
                {"id" : 4, "msg": "Find client", "final": False, "next" : [
                    { "msg" : "<name>", "final" : True, "type": "client3", "method" : self._mainController._clientRepository.findClients}
                ]},
                {"id" : 5, "msg": "Print", "final" : True, "type" : "printClients"}
            ]},
            {"id" : 2, "msg": "Movie commands", "final" : False, "next": [
                {"id" : 1, "msg": "Add movie", "final" : False, "next" : [
                    { "msg" : "<title> <description> <genre>", "final" : True, "type": "movie1", "method" : self._mainController._movieRepository.addMovie}
                ]},
                {"id" : 2, "msg": "Remove movie", "final" : False, "next" : [
                    { "msg" : "<title>", "final" : True, "type": "movie2", "method" : self._mainController.removeMovie}
                ]},
                {"id" : 3, "msg": "Replace movie", "final": False, "next" : [
                    { "msg" : "<replacedTitle> <newTitle> <newDescription> <newGenre>", "final" : True, "type": "movie3", "method" : self._mainController.replaceMovie}
                ]},
                {"id" : 4, "msg": "Find movie", "final" : False, "next" : [
                    { "msg" : "<title> <description> <genre>", "final" : True, "type": "movie4", "method" : self._mainController._movieRepository.findMovies}
                ]},
                {"id" : 5, "msg": "Print", "final" : True, "type" : "printMovies"}
            ]},
            {"id" : 3, "msg": "Rental commands", "next": [
                {"id" : 1, "msg": "Rent movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <rentedDate> <dueDate>", "final" : True, "type": "rental1", "method" : self._mainController._rentalRepository.rentMovie}
                ]},
                {"id" : 2, "msg": "Return movie", "final" : False, "next" : [
                    { "msg" : "<clientName> <movieName> <returnedDate>", "final" : True, "type": "rental2", "method" : self._mainController._rentalRepository.returnMovie}
                ]},
                {"id" : 3, "msg": "Print", "final" : True, "type" : "printRentals"}
            ]},
            {"id" : 4, "msg": "Stats commands", "next": [
                {"id" : 1, "msg": "Most rented movies", "final" : True, "next" : [
                    {"type": "stats1", "msg": "Printing most rented movies:", "final" : True, "method": self._mainController._rentalRepository.mostRentedMovies}
                ]},
                {"id" : 2, "msg": "Most active clients", "final" : True, "next" : [
                    {"type": "stats2", "msg": "Printing most active clients:", "final" : True, "method": self._mainController._rentalRepository.mostActiveClients}
                ]},
                {"id" : 3, "msg": "All current rentals & all currently rented movies", "final" : True, "next" : [
                    {"type": "stats3", "msg": "Printing your stats:", "final" : True, "method": self._mainController._rentalRepository.rentalsAndMoviesCurrentlyRented}
                ]},
                {"id" : 4, "msg": "Late rentals sorted by the delay", "final" : True, "next" : [
                    {"type": "stats4", "msg": "Printing your stats:", "final" : True, "method": self._mainController._rentalRepository.currentlyRentedUnreturnedMovies}
                ]}
            ]},
             {"id" : 5, "msg": "Undo / Redo commands", "next": [
                {"id" : 1, "msg": "Undo", "final" : True, "next" : [
                    {"type": "undo", "msg": "Undo last command:", "final" : True, "method": self._mainController.undoState}
                ]},
                {"id" : 2, "msg": "Redo", "final" : True, "next" : [
                    {"type": "redo", "msg": "Redo the last undo:", "final" : True, "method": self._mainController.redoState}
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
                if menu[inputNumber-1]["type"] == "printClients":
                    print(self._mainController._clientRepository)
                if menu[inputNumber-1]["type"] == "printMovies":
                    print(self._mainController._movieRepository)
                if menu[inputNumber-1]["type"] == "printRentals":
                    print(self._mainController._rentalRepository)

                self.showMenu(self._menu)
                return

            self.showMenu(menu[inputNumber - 1]["next"])
        else:
            print("\n---MENU----")
            print(str(menu[0]["msg"]))

            if menu[0]["type"] == "client0":
                clientObj = Client(input("Name: "))
                menu[0]["method"](clientObj)
                self._mainController.saveState("addClient", clientObj)
            if menu[0]["type"] == "client1":
                clientObj = Client(input("Name: "))
                menu[0]["method"](clientObj)
                self._mainController.saveState("removeClient", clientObj)
            if menu[0]["type"] == "client2":
                clientOldNameObj = Client(input("oldName: "))
                clientNewNameObj = Client(input("newName: "))
                menu[0]["method"](clientOldNameObj, clientNewNameObj)
                self._mainController.saveState("replaceClient", {"oldName": clientOldNameObj, "newName": clientNewNameObj})
            if menu[0]["type"] == "client3":
                print(menu[0]["method"](Client(input("Name: "))))
                self._mainController.saveState()
            if menu[0]["type"] == "movie1":
                movieObj = Movie(input("Title: "), input("Description: "), input("Genre: "))
                menu[0]["method"](movieObj)
                self._mainController.saveState("addMovie", movieObj)
            if menu[0]["type"] == "movie2":
                movieObj = Movie(input("Title: "), "", "")
                movieId = self._mainController._movieRepository.findMovie(movieObj)
                movieSavedObj = self._mainController._movieRepository.getMovieById(movieId)
                menu[0]["method"](movieObj)
                self._mainController.saveState("removeMovie", movieSavedObj)
            if menu[0]["type"] == "movie3":
                movieOldObj = Movie(input("Replaced title: "), "", "")
                movieNewObj = Movie(input("Title: "), input("Description: "), input("Genre: "))

                movieOldId = self._mainController._movieRepository.findMovie(movieOldObj)
                movieOldSavedObj = self._mainController._movieRepository.getMovieById(movieOldId)

                menu[0]["method"](movieOldObj, movieNewObj)
                self._mainController.saveState("replaceMovie",{"oldMovie": movieOldSavedObj, "newMovie": movieNewObj})
            if menu[0]["type"] == "movie4":
                print(menu[0]["method"](Movie(Utils.bypassValidation(input("Title: ")), Utils.bypassValidation(input("Description: ")), Utils.bypassValidation(input("Genre: ")))))
            if menu[0]["type"] == "rental1":
                menu[0]["method"](Rental(self._mainController._clientRepository.getClientIdByName(input("Client name: ")), self._mainController._movieRepository.getMovieIdByName(input("Movie name: ")), input("Rented date: "), input("Due date: "), ""))
            if menu[0]["type"] == "rental2":
                menu[0]["method"](Rental(self._mainController._clientRepository.getClientIdByName(input("Client name: ")), self._mainController._movieRepository.getMovieIdByName(input("Movie name: ")), "", "", str(input("Returned date: "))))
            if menu[0]["type"] == "stats1":
                print(self.mostRentedMoviesUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats2":
                print(self.mostActiveClientsUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats3":
                print(self.rentalsAndMoviesCurrentlyRentedUI(menu[0]["method"]()))
            if menu[0]["type"] == "stats4":
                print(self.currentlyRentedUnreturnedMoviesUI(menu[0]["method"]()))
            if menu[0]["type"] == "undo" or menu[0]["type"] == "redo":
                 menu[0]["method"]()

            self._mainController.saveToRepository()
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
            out = out + self._mainController._movieRepository.getMovieById(crt[0]).getTitle() + ": " + str(crt[1]) + "\n"

        return out

    def mostActiveClientsUI(self, obj):
        out = "\n\nName: Nr of movies rented\n"

        for crt in obj:
            out = out + self._mainController._clientRepository.getClientById(crt[0]).getName() + ": " + str(crt[1]) + "\n"

        return out

    def rentalsAndMoviesCurrentlyRentedUI(self, obj):
        out = "\n\nCurrent rentals:\n"
        out = out + "ID: ClientName\n"
        for clientId in obj.keys():
            out = out + str(clientId) + ": " + self._mainController._clientRepository.getClientById(clientId).getName() + "\n"
            out = out + "  ID: Movie Title\n"
            for movieId in obj[clientId]:
                out = out + "  " + str(movieId) + ": " + self._mainController._movieRepository.getMovieById(movieId).getTitle()  + "\n"
            out = out + "\n"

        return out

    def currentlyRentedUnreturnedMoviesUI(self, obj):
        out = "\n\nID: Movie Title, Nr. of days passed\n"

        for crt in obj:
            out = out + str(crt.getMovieId()) +": " + self._mainController._movieRepository.getMovieById(crt.getMovieId()).getTitle() + ", " + str((crt.getReturnedDate() - crt.getDueDate()).days) + " days passed\n"

        return out