class Movie(object):
    def __init__(self, id, title, description, genre_ids, imdb_rating, tmdb_rating, imdb_url):
        self.id = id
        self.title = title
        self.description = description
        self.genre_ids = genre_ids
        self.imdb_rating = imdb_rating
        self.tmdb_rating = tmdb_rating
        self.imdb_url = imdb_url

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self):
        return "id: " + self.id + '\t' + \
               "title: " + self.title + '\t' + \
               "description: " + self.description + "\t" + \
               "genre_ids:" + self.genre_ids + "\t" + \
               "imdb_rating: " + self.imdb_rating + "\t" + \
               "tmdb_rating: " + self.tmdb_rating + "\t" + \
               "imdb_url: " + self.imdb_url + "\n"

