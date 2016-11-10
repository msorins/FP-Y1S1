__author__ = 'sorynsoo'

from movieRental.Model.movie import *
from movieRental.Model.client import *
from movieRental.Model.rental import *

class Tests:
    def __init__(self, movieController, clientController, rentalController):
        self._movieController = movieController
        self._clientController = clientController
        self._rentalController = rentalController

        self.populateValues()
        self.addClientTest()
        self.removeClientTest()
        self.replaceClientTest()
        self.addMovieTest()
        self.removeMovieTest()
        self.replaceMovieTest()
        self.getMovieIdByNameTest()
        self.rentMovieTest()
        self.returnMovieTest()

    def populateValues(self):
        names = ["Sorin", "Andreea", "Gheorghe", "Alex", "Lupi", "Stefan", "George", "Denis", "Sorpasc", "Costel"]
        for crt in names:
            self._clientController.addClient(Client(crt))

        shows = [
            ["Breaking Bad", "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine", "Crime"],
            ["Game of Thrones", "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise to power", "Adventure"],
            ["The Walking Dead", "Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living", "Horror"],
            ["The Flash", "After being struck by lightning, Barry Allen wakes up from his coma to discover he's been given the power of super speed, becoming a superhero, The Flash, fighting crime in Central City", "Action"],
            ["Supernatural", "Two brothers follow their father's footsteps as hunters fighting evil supernatural beings of many kinds including monsters, demons, and gods that roam the earth", "Drama/Action"],
            ["Lucifer", "Lucifer takes up residence in Los Angeles", "Crime/Drama/Fantasay"],
            ["Vikings", "The world of the Vikings is brought to life through the journey of Ragnar Lothbrok, the first Viking to emerge from Norse legend and onto the pages of history - a man on the edge of myth", "Action/Drama/History"],
            ["The Blacklist", "A new FBI profiler, Elizabeth Keen, has her entire life uprooted when a mysterious criminal, Raymond Reddington, who has eluded capture for decades, turns himself in and insists on speaking only to her", "Crime/Drama/Mistery"],
            ["Modern Family", "Three different, but related families face trials and tribulations in their own uniquely comedic ways", "Comedy/Romance"],
            ["Suits", "On the run from a drug deal gone bad, Mike Ross, a brilliant college-dropout, finds himself a job working with Harvey Specter, one of New York City's best lawyers", "Comedy/Drama"],
            ["Arrow", "Spoiled billionaire playboy Oliver Queen is missing and presumed dead when his yacht is lost at sea. He returns five years later a changed man, determined to clean up the city as a hooded vigilante armed with a bow", "Action/Adventure"]
        ]

        for crt in shows:
            self._movieController.addMovie(Movie(crt[0], crt[1], crt[2]))

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Supernatural"),"1.11.2016","10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Vikings"),"1.11.2016","10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"15.11.2016","20.11.2016", ""))
        self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"","", "22.11.2016"))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Costel"), self._movieController.getMovieIdByName("The Flash"),"1.12.2016","17.12.2016", ""))

    def addClientTest(self):
        self._clientController.addClient(Client("zuckerberg"))
        assert self._clientController.findClient(Client("zuckerberg")) != -1

        self._clientController.addClient(Client("gates"))
        assert self._clientController.findClient(Client("gates")) != -1


        try:
            self._clientController.addClient(Client("zuckerberg"))
        except Exception as e:
            assert str(e) == "There already exists a user with this name"

        try:
            self._clientController.addClient(Client(""))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def removeClientTest(self):
        self._clientController.removeClient(Client("zuckerberg"))
        assert self._clientController.findClient(Client("zuckerberg")) == -1

        self._clientController.removeClient(Client("gates"))
        assert self._clientController.findClient(Client("gates")) == -1


        try:
            self._clientController.addClient(Client("zuckerberg"))
        except Exception as e:
            assert str(e) == "Client does not exist, can't remove"

        try:
            self._clientController.addClient(Client(""))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def replaceClientTest(self):
        self._clientController.replaceClient(Client("zuckerberg"), Client("mark"))
        assert self._clientController.findClient(Client("zuckerberg")) == -1
        assert self._clientController.findClient(Client("mark")) != -1

        self._clientController.addClient(Client("gates"))
        self._clientController.replaceClient(Client("gates"), Client("bill"))
        assert self._clientController.findClient(Client("gates")) == -1
        assert self._clientController.findClient(Client("bill")) != -1


        try:
            self._clientController.replaceClient(Client("zuckerberg"), Client("bla"))
        except Exception as e:
            assert str(e) == "Client does not exist"

        try:
            self._clientController.replaceClient(Client(""), Client(""))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def getClientIdByName(self):
        assert self._clientController.getClientIdByName("Sorin") == 0
        assert self._clientController.getClientIdByName("Andreea") == 1
        assert self._clientController.getClientIdByName("Gheorghe") == 2
        assert self._clientController.getClientIdByName("Alex") == 3

        try:
            self._clientController.getClientIdByName("BZCWE")
        except Exception as e:
            assert str(e) == "User not found"

    def addMovieTest(self):
        self._movieController.addMovie(Movie("Titanic", "Ship...", "Drama"))
        assert self._movieController.findMovie(Movie("Titanic", "", "")) != -1

        self._movieController.addMovie(Movie("Family guy", "In a wacky Rhode Island town, a dysfunctional family strive to cope with everyday life as they are thrown from one crazy scenario to another.", "Comedy"))
        assert self._movieController.findMovie(Movie("Family guy", "", "")) != -1


        try:
            self._movieController(Movie("", "", ""))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def removeMovieTest(self):
        self._movieController.removeMovie(Movie("Titanic", "", ""))
        assert self._movieController.findMovie(Movie("Titanic", "", "")) == -1

        self._movieController.removeMovie(Movie("Family guy", "", ""))
        assert self._movieController.findMovie(Movie("Family guy", "", "")) == -1


        try:
            self._movieController.removeMovie(Movie("ABCD", "", ""))
        except Exception as e:
            assert str(e) == "Requested movie does not exist"

        try:
            self._movieController.removeMovie(Movie("", "", ""))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def replaceMovieTest(self):
        self._movieController.addMovie(Movie("Titanic", "Ship...", "Drama"))
        self._movieController.replaceMovie(Movie("Titanic", "", ""), Movie("Titans", "boom boom boom", "action"))
        assert self._movieController.findMovie(Movie("Titans", "", ""))

        self._movieController.addMovie(Movie("Family guy", "In a wacky Rhode Island town, a dysfunctional family strive to cope with everyday life as they are thrown from one crazy scenario to another.", "Comedy"))
        self._movieController.replaceMovie(Movie("Family guy", "", ""), Movie("The Simpsons", "The satiric adventures of a working-class family in the misfit city of Springfield.", "animation"))
        assert self._movieController.findMovie(Movie("The Simpsons", "", ""))

        try:
            self._movieController.replaceMovie(Movie("XYZW", "", ""), Movie("Bla", "Description", "Action"))
        except Exception as e:
            assert str(e) == "Requested movie does not exist"

        try:
            self._movieController.replaceMovie(Movie("", "", ""), Movie("Bla", "Description", "Action"))
        except Exception as e:
            assert str(e) == "Invalid input, empty input"

    def getMovieIdByNameTest(self):
        assert self._movieController.getMovieIdByName("Breaking Bad") == 0
        assert self._movieController.getMovieIdByName("Game of Thrones") == 1
        assert self._movieController.getMovieIdByName("The Walking Dead") == 2

        try:
            self._movieController.getMovieIdByName("blablaE")
        except Exception as e:
            assert str(e) == "Movie not found"

    def rentMovieTest(self):
        crtLen = len(self._rentalController)

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Suits"), "15.11.2016", "20.11.2016", ""))
        assert len(self._rentalController) == crtLen + 1

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Gheorghe"), self._movieController.getMovieIdByName("Suits"), "15.09.2016", "25.11.2016", ""))
        assert len(self._rentalController) == crtLen + 2

        #Testing in this way also canUserRent()
        try:
            self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Arrow"), "15.11.2016", "20.11.2016", ""))
        except Exception as e:
            assert str(e) == "User cannot rent movie due to the fact that is untrustworty"

        try:
            self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("ZAAP"), self._movieController.getMovieIdByName("Arrow"), "15.11.2016", "20.11.2016", ""))
        except Exception as e:
            assert str(e) == "Client not found"

        try:
            self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("BZZP"), "15.11.2016", "20.11.2016", ""))
        except Exception as e:
            assert str(e) == "Movie not found"

    def returnMovieTest(self):
        crtLen = len(self._rentalController)
        try:
            self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Suits"), "", "", "21.11.2016"))
            self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Gheorghe"), self._movieController.getMovieIdByName("Suits"), "", "", "23.11.2016"))
        except Exception as e:
            assert False

        assert len(self._rentalController) == crtLen

        try:
            self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("BlbLA"), self._movieController.getMovieIdByName("Suits"), "", "", "21.11.2016"))
        except Exception as e:
            assert str(e) == "Client not found"

        try:
            self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("BlaBla"), "", "", "21.11.2016"))
        except Exception as e:
            assert str(e) == "Movie not found"

        try:
            self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName(""), self._movieController.getMovieIdByName("Suits"), "", "", "21.11.2016"))
        except Exception as e:
            assert str(e) == "Client not found"


