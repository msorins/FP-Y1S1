from movieRental.Model.movie import *

class MovieController():
    def __init__(self):
        self._movieList = []

    def addMovie(self, movie):
        if(type(movie) == Movie):
            self._movieList.append(movie)
            print(movie.getTitle() + " added to the movie list")
        else:
            raise TypeError("Invalid movie format")

    def removeMovie(self, movie):
        searchedIndex = self.findMovie(movie)
        if searchedIndex == -1:
            raise RuntimeError("Requested movie does not exist")

        self._movieList.pop(searchedIndex)

    def replaceMovie(self, movieOld, movieNew):
        searchedIndex = self.findMovie(movieOld)
        if searchedIndex == -1:
            raise RuntimeError("Requested movie does not exist")

        self._movieList[searchedIndex] = movieNew

    def findMovie(self, movie):
        '''
        :param movie: a Movie type object
        :return:
        '''
        for i in range(len(self._movieList)):
            if self._movieList[i].getTitle() == movie.getTitle():
                return i
        return -1

    def getMovieIdByName(self, title):
        for crt in self._movieList:
            if crt.getTitle() == title:
                return crt.getMovieId()

        raise RuntimeError("Movie not found")
    def __iter__(self):
        for elem in self._movieList:
            yield elem

    def __str__(self):
        msg = "\nID | TITLE | GENRE\n"
        for crt in self._movieList:
            msg += str(crt.getMovieId()) + ": " + str(crt.getTitle()) + ",  " + str(crt.getGenre())
            msg += "\n"
        return msg

    def __len__(self):
        return len(self._movieList)