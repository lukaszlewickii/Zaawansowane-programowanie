import csv
import pandas as pd

df1 = pd.read_csv(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\links.csv')
df2 = pd.read_csv(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\movies.csv')
df3 = pd.read_csv(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\ratings.csv')
df4 = pd.read_csv(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\tags.csv')

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

#file = open(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\movies.csv', encoding="utf8")
        

with open(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\movies.csv', encoding="utf8") as movies:
    reader_obj = csv.DictReader(movies)

    for row in reader_obj:
        print(row)

"""
movies = csv.DictReader(open(r'd:\Desktop\Zaawansowane programowanie\Laborki 7 - 8.11.22\movies.csv'))
print(movies)
"""

#print(Movie.__dict__)
