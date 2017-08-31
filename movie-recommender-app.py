# https://api.themoviedb.org/3/discover/movie?api_key=e2c84bd4529ef2b20608f45305fd3bc1&language=en-US&region=US&sort_by=popularity.desc&include_adult=true&page=1&release_date.gte=2017-08-01&with_release_type=4
# https://api.themoviedb.org/3/movie/550?api_key=e2c84bd4529ef2b20608f45305fd3bc1
from service.movie_recomennder_service import get_movies

if __name__ == '__main__':
    # description = get_movie_description(550)
    # movies = get_discovered_movies()
    # print(movies)
    get_movies()
