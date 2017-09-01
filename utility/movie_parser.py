from model.Movie import Movie


def parse_data_to_Movie(data, imdb_rating=None, imdb_url=None):
    return Movie(str(data['id']), data['title'], data['overview'], str(data['genre_ids']),
                 str(imdb_rating), str(data['vote_average']), imdb_url)
