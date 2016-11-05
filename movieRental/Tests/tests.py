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

    def populateValues(self):
        names = ["Sorin", "Andreea", "Gheorghe", "Alex", "Lupi", "Stefan", "George", "Denis"]
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
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"15.11.2016","20.11.2016", ""))
        self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"","", "22.11.2016"))


