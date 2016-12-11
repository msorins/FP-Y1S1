from movieRental.Model.movie import *
import copy

class MovieRepository():
    def __init__(self):
        '''
        Instantiates the MovieRepository with an empty list of movies
        '''
        self._movieList = []

    def addMovie(self, movie):
        '''
        Add a movie to the list
        :param movie: Movie Object
        '''
        if(type(movie) == Movie):
            self._movieList.append(movie)
            #print(movie.getTitle() + " added to the movie list")
        else:
            raise TypeError("Invalid movie format")

    def removeMovie(self, movie):
        '''
        Removes a movie from the list
        :param movie: Movie Object
        '''
        searchedIndex = self.findMovie(movie)
        if searchedIndex == -1:
            raise RuntimeError("Requested movie does not exist")

        self._movieList.pop(searchedIndex)

    def replaceMovie(self, movieOld, movieNew):
        '''
        Replaces a movie with anther one
        :param movieOld: Movie Object
        :param movieNew: Movie Object
        '''
        searchedIndex = self.findMovie(movieOld)
        if searchedIndex == -1:
            raise RuntimeError("Requested movie does not exist")

        self._movieList[searchedIndex] = movieNew

    def findMovies(self, movie):
        '''
        Finds multiple movies by multiple attributes
        :param movie: Movie Object
        :return: the list of movies that are found
        '''
        result = MovieRepository()

        for i in range(len(self._movieList)):
           #Search by case-insensitive + partial name
           if Utils().findPartial(self._movieList[i].getTitle(), movie.getTitle()):
               result.addMovie(self._movieList[i])
               continue
           #Search by case-insensitive + partial description
           if Utils().findPartial(self._movieList[i].getDescription(), movie.getDescription()):
               result.addMovie(self._movieList[i])
               continue
           #Search by case-insensitive + partial genre
           if Utils().findPartial(self._movieList[i].getGenre(), movie.getGenre()):
               result.addMovie(self._movieList[i])

        return result

    def findMovie(self, movie):
        '''
        Finds just only one movie (exact match)
        :param movie: a movie object
        :return: an integer representing the id or -1 if it is not found
        '''
        for i in range(len(self._movieList)):
            if self._movieList[i].getTitle() == movie.getTitle():
                return i
        return -1

    def getMovieIdByName(self, title):
        '''
        :param title: string
        :return: an integer representing the id or an exception is raised if it is nout found
        '''
        for crt in self._movieList:
            if crt.getTitle() == title:
                return crt.getMovieId()

        raise RuntimeError("Movie not found")

    def getMovieById(self, id):
        '''
        :param id: an integer representing the movie id
        :return: a movie object
        '''
        for crt in self._movieList:
            if crt.getMovieId() == id:
                return crt

        raise RuntimeError("Movie not found")

    def __iter__(self):
        '''
        Enables capability of iteration over the Repo
        '''
        for elem in self._movieList:
            yield elem

    def __str__(self):
        '''
        :return: a nicely formatted string with the elements from the Repo
        '''
        msg = "\nID | TITLE | GENRE\n"
        for crt in self._movieList:
            msg += str(crt.getMovieId()) + ": " + str(crt.getTitle()) + ",  " + str(crt.getGenre())
            msg += "\n"
        return msg

    def __len__(self):
        '''
        :return: the number of elements from the repo
        '''
        return len(self._movieList)