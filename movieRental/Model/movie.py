
from movieRental.Utils.utils import *

class Movie:
    idCount = 0

    def __init__(self, title, description, genre):
        '''
        Instantiates the movie class with 3 attributes
        :param title: string
        :param description: string
        :param genre: string
        '''
        self._utilsObject = Utils()

        self.setMovieId()
        self.setTitle(title)
        self.setDescription(description)
        self.setGenre(genre)

    def setMovieId(self):
        '''
        Setter
        :return: sets the movie id automatically
        '''
        self._movieId = Movie.idCount
        Movie.idCount = Movie.idCount + 1

    def setManuallyMovieId(self, id):
        '''
        Setter
        :param id: integer
        :return: sets the movie id manually (override)
        '''
        self._movieId = id

    def getMovieId(self):
        '''
        Getter
        :return: return the movieId
        '''
        return self._movieId

    def setTitle(self, title):
        '''
        Setter
        :param title: string
        :return: sets the movie title
        '''
        self._utilsObject.nonEmptyAndMoreThanThree(title)
        self._title = title

    def getTitle(self):
        '''
        Getter
        :return: the movie title
        '''
        return self._title

    def setDescription(self, description):
        '''
        Setter
        :param description: string
        :return: sets the movie title
        '''
        #self._utilsObject.nonEmptyAndMoreThanThree(description)
        self._description = description

    def getDescription(self):
        '''
        Getter
        :return: the movie description
        '''
        return self._description

    def setGenre(self, genre):
        '''
        Setter
        :param genre: string
        :return: sets the movie genre
        '''
        #self._utilsObject.nonEmptyAndMoreThanThree(genre)
        self._genre = genre

    def getGenre(self):
        '''
         Getter
        :return: the movie genre
        '''
        return self._genre
