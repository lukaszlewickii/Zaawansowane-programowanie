from flask_restful import Resource

class Rating(Resource):
    def __init__(self, userId, moveId, rating, timestamp):
        self.userId = userId
        self.moveId = moveId
        self.rating = rating
        self.timestamp = timestamp
        
def RatingsData(file):
    ratings = []
    with open('data_laborki_8.11/ratings.csv', 'r', encoding = 'utf-8') as file:
        for row in file:
            modifiedData = row.split(",")
            ratings.append(Rating(modifiedData[0], modifiedData[1], modifiedData[2], modifiedData[3]).__dict__)
        return ratings
        