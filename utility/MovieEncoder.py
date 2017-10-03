from flask.json import JSONEncoder
from model.Movie import Movie


class MovieEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Movie):
            return {'id': o.id,
                    'title': o.title,
                    'description': o.description,
                    'genre_ids': o.genre_ids,
                    'imdb_rating': o.imdb_rating,
                    'tmdb_rating': o.tmdb_rating,
                    'release_date': o.release_date,
                    'imdb_url': o.imdb_url}
        return super(MovieEncoder, self).default(o)
