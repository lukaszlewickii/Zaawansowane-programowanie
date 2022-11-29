from flask import Flask
from link_class import LinksData
from movie_class import MoviesData
from rating_class import RatingsData
from tag_class import TagsData

app = Flask(__name__)

@app.route("/links")
def links():
    return LinksData('data_laborki_8.11/links.csv')

@app.route("/movies")
def movies():
    return MoviesData('data_laborki_8.11/movies.csv')

@app.route("/ratings")
def ratings():
    return RatingsData('data_laborki_8.11/ratings.csv')

@app.route("/tags")
def tags():
    return TagsData('data_laborki_8.11/tags.csv')

if __name__ == '__main__':
    app.run()