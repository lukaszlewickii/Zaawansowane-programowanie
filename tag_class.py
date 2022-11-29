from flask_restful import Resource

class Tag(Resource):
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

def TagsData(file):
    tags = []
    with open('data_laborki_8.11/tags.csv', 'r', encoding = 'utf-8') as file:
        for row in file:
            modifiedData = row.split(",")
            tags.append(Tag(modifiedData[0], modifiedData[1], modifiedData[2], modifiedData[3]).__dict__)
        return tags