from model.Movie import Movie


def parse_data_to_Movie(data, imdb_rating=None, imdb_url=None):
    return Movie(data['title'], data['overview'], data['genre_ids'], imdb_rating, data['vote_average'], imdb_url)
