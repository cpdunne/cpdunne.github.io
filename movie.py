class Movie:
    def __init__(self, title, release_year, director, ratings = [], average_rating = 0.0):
        self.__title = str(title)
        self.__release_year = int(release_year)
        self.__director = str(director)
        self.__ratings = list(ratings)
        self.__average_rating = float(average_rating)

    def getdatitle(self):
        return self.__title

    def __str__(self):
        return (f'Title: {self.__title} \tYear: {self.__release_year} \tDirector: {self.__director}')

    def add_rating(self, bingus):
        self.__ratings.append(int(bingus))

    def calc_average_rating(self):
        # Void function - does not return anything
        avg = 0
        count = 0
        for i in self.__ratings:
            avg += int(i)
            count += 1
        self.__average_rating = avg / count

    def getRatings(self):
        return self.__ratings

    def getAverageRating(self):
        return self.__average_rating

    # Define attributes and methods for a Movie class,
    #    as specified in the instructions
    # The attributes should be PRIVATE
