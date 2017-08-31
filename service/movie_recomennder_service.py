from utility.movie_parser import parse_data_to_Movie
from utility.tmdb_utils import get_discovered_movies


def get_movies():
    movies = get_discovered_movies()
    for movie_data in movies:
        rating = "imdb_rating"
        url = "imdb_url"
        movie = parse_data_to_Movie(movie_data, rating, url)
        print(movie)