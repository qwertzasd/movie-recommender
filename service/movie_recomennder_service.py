from utility.movie_parser import parse_data_to_Movie
from utility.tmdb_utils import get_discovered_movies, get_movie_description

IMDB_URL = "http://www.imdb.com/title/"


def get_movies():
    movies = get_discovered_movies()
    result = []
    for movie_data in movies:
        movie_id = movie_data['id']
        movie_description = get_movie_description(movie_id)
        imdb_rating = "imdb_rating"
        imdb_id = movie_description['imdb_id']
        imdb_url = IMDB_URL + str(imdb_id) if imdb_id is not None and len(imdb_id) > 0 else "NA"
        movie = parse_data_to_Movie(movie_data, imdb_rating, imdb_url)
        result.append(movie)
    return result
