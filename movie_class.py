from flask_restful import Resource

class Movie(Resource):
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres
        
def MoviesData(file):
    movies = []
    with open('data_laborki_8.11/movies.csv', 'r', encoding = 'utf-8') as file:
        for row in file:
            modifiedData = row.split(",")
            movies.append(Movie(modifiedData[0], modifiedData[1], modifiedData[2]).__dict__)
        return movies
        
