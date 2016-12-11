__author__ = 'sorynsoo'

from movieRental.Model.movie import *
from movieRental.Model.client import *
from movieRental.Model.rental import *

class PopulateDB:
    def __init__(self, movieController, clientController, rentalController):
        self._movieController = movieController
        self._clientController = clientController
        self._rentalController = rentalController

        self.populateValues()


    def populateValues(self):
        names = ["Sorin", "Andreea", "Gheorghe", "Alex", "Lupi", "Stefan", "George", "Denis", "Sorpasc", "Costel", "Elena","Inger","Yahaira", "Annamaria","Lonna","Darrel","Edmundo","Grady","Carylon","Maritza","Ardith","Benito","Napoleon","Buena","Filomena","Jule","Melonie","Cris","Flor","Annelle","Ronda","Nick","Claris","Marita","Maryanna","America","Lurlene","Rosetta","Verna" ,"Catrina", "Georgeta" ]
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
            ["Arrow", "Spoiled billionaire playboy Oliver Queen is missing and presumed dead when his yacht is lost at sea. He returns five years later a changed man, determined to clean up the city as a hooded vigilante armed with a bow", "Action/Adventure"],
            ["Supergirl", "n an effort to protect Kal-El, the future Superman, a 13-year old Kara Zor-El was launched from Krypton moments..", "Action"],
            ["The Young and the Restless", "The Young and the Restless revolves around the rivalries, romances, hopes and fears of the residents of the fictional Midwestern..", "Comedy"],
            ["The Big Bang Theory", "Created by writer/producers Chuck Lorre (of Two and a Half Men) and Bill Prady (of Gilmore Girls) comes The Big", "Comedy/Romance"],
            ["Grey's Anatomy", "Grey's Anatomy is a medical drama about a group of surgeons working at Seattle Grace Hospital. The show centers around", "Medical/Drama"],
            ["Criminal Minds", "The Behavioral Analysis Unit consists of an elite team of FBI profilers who analyze the country's most twisted criminal minds", "Drama"],
            ["The Vampire Diaries", "The Vampire Diaries is based on a novel series penned by L.J. Smith where you are given the insight into...", "SF/Romance"],
            ["Survivor", "The rules of Survivor are simple: Americans are abandoned in the middle of some of the most unforgiving places on", "Action"],
            ["Gotham", "Explores the origin stories of Commissioner James Gordon.  He is still a detective but he has yet to meet Batman and the villains who made Gotham City so famous", "Action/Adventure"],
            ["The Simpsons", "This is the 25th Treehouse of Horror in the Simpsons organized by Matt Groening. It is divided in three parts", "Comedy/Animation"],
            ["Teen Wolf", "MTV's reboot of the classic 1980s cult movie Teen Wolf. Scott is a typical high school student until one night", "SF/Adventure/Drama"],
            ["Elementary", "Elementary is a CBS television series based on Sir Arthur Conan Doyle's Sherlock Holmes detective stories with contemporary twists.", "Comedy"],
            ["The Chew", "The Chew will focus on food from every regard - as a source of health, happiness, family, friendship, fitness, romance,", "Action/Adventure"],
            ["Bones", "From executive producers Barry Josephson and Hart Hanson comes the darkly amusing drama Bones, inspired by real-life forensic anthropologist and", "Action/Horror"],
            ["American Dad!", "American Dad! from Family Guy creator, Seth MacFarlane, is the animated story of Stan Smith, who works for the CIA", "Comedy/Animation"],
            ["Blue Bloods", "Blue Bloods is a CBS police drama by Robin Green and Mitchell Burgess, known for their work on the long", "Action"]


        ]

        for crt in shows:
            self._movieController.addMovie(Movie(crt[0], crt[1], crt[2]))

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Supernatural"),"1.11.2016","10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Vikings"),"1.11.2016","10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"15.11.2016","20.11.2016", ""))
        self._rentalController.returnMovie(Rental(self._clientController.getClientIdByName("Andreea"), self._movieController.getMovieIdByName("Vikings"),"","", "22.11.2016"))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Costel"), self._movieController.getMovieIdByName("The Flash"),"1.12.2016","17.12.2016", ""))

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Georgeta"), self._movieController.getMovieIdByName("Supernatural"), "1.11.2016", "10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("America"), self._movieController.getMovieIdByName("Supernatural"), "2.11.2016", "15.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Verna"), self._movieController.getMovieIdByName("Supernatural"), "3.11.2016", "20.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Napoleon"), self._movieController.getMovieIdByName("Supernatural"), "4.11.2016", "22.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Grady"), self._movieController.getMovieIdByName("Supernatural"), "5.11.2016", "24.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Sorin"), self._movieController.getMovieIdByName("Survivor"), "5.11.2016", "24.11.2016", ""))

        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Georgeta"),
                                                self._movieController.getMovieIdByName("Gotham"), "1.11.2016",
                                                "10.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("America"),
                                                self._movieController.getMovieIdByName("Survivor"), "2.11.2016",
                                                "15.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Verna"),
                                                self._movieController.getMovieIdByName("Bones"), "3.11.2016",
                                                "20.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Napoleon"),
                                                self._movieController.getMovieIdByName("Blue Bloods"), "4.11.2016",
                                                "22.11.2016", ""))
        self._rentalController.rentMovie(Rental(self._clientController.getClientIdByName("Grady"),
                                                self._movieController.getMovieIdByName("The Chew"), "5.11.2016",
                                                "24.11.2016", ""))
