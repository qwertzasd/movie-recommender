class Movie(object):

    def __init__(self, title, description, genre_ids, imdb_rating, tmdb_rating, imdb_url):
        self.title = title
        self.description = description
        self.genre_ids = genre_ids
        self.imdb_rating = imdb_rating
        self.tmdb_rating = tmdb_rating
        self.imdb_url = imdb_url

    def __str__(self) -> str:
        return super().__str__()
