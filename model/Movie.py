class Movie(object):
    def __init__(self, id, title, description, genre_ids, imdb_rating, tmdb_rating, release_date, imdb_url):
        self.id = id
        self.title = title
        self.description = description
        self.genre_ids = genre_ids
        self.imdb_rating = imdb_rating
        self.tmdb_rating = tmdb_rating
        self.release_date = release_date
        self.imdb_url = imdb_url

    def serialize(self):
        return "id: " + self.id + '\t' + \
               "title: " + self.title + '\t' + \
               "description: " + self.description + "\t" + \
               "genre_ids:" + self.genre_ids + "\t" + \
               "imdb_rating: " + self.imdb_rating + "\t" + \
               "tmdb_rating: " + self.tmdb_rating + "\t" + \
               "release_date: " + self.release_date + "\t" + \
               "imdb_url: " + self.imdb_url + "\n"

    def __str__(self):
        return "id: " + self.id + '\t' + \
               "title: " + self.title + '\t' + \
               "description: " + self.description + "\t" + \
               "genre_ids:" + self.genre_ids + "\t" + \
               "imdb_rating: " + self.imdb_rating + "\t" + \
               "tmdb_rating: " + self.tmdb_rating + "\t" + \
               "release_date: " + self.release_date + "\t" + \
               "imdb_url: " + self.imdb_url + "\n"

