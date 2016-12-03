
from movieRental.Utils.utils import *

class Movie:
    idCount = 0

    def __init__(self, title, description, genre):
        self._utilsObject = Utils()

        self.setMovieId()
        self.setTitle(title)
        self.setDescription(description)
        self.setGenre(genre)

    def setMovieId(self):
        self._movieId = Movie.idCount
        Movie.idCount = Movie.idCount + 1

    def setManuallyMovieId(self, id):
        self._movieId = id

    def getMovieId(self):
        return self._movieId

    def setTitle(self, title):
        self._utilsObject.nonEmptyAndMoreThanThree(title)
        self._title = title

    def getTitle(self):
        return self._title

    def setDescription(self, description):
        #self._utilsObject.nonEmptyAndMoreThanThree(description)
        self._description = description

    def getDescription(self):
        return self._description

    def setGenre(self, genre):
        #self._utilsObject.nonEmptyAndMoreThanThree(genre)
        self._genre = genre

    def getGenre(self):
        return self._genre
