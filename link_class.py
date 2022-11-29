from flask_restful import Resource

class Link(Resource):
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId
        
def LinksData(file):
    links = []
    with open('data_laborki_8.11/links.csv', 'r', encoding = 'utf-8') as file:
        for row in file:
            splittedLines = row.split(",")
            links.append(Link(splittedLines[0], splittedLines[1], splittedLines[2]).__dict__)
        return links
    