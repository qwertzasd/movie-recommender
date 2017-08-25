import requests
import json

API_KEY = "e2c84bd4529ef2b20608f45305fd3bc1"
ACCESS_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' \
               '.eyJhdWQiOiJlMmM4NGJkNDUyOWVmMmIyMDYw' \
               'OGY0NTMwNWZkM2JjMSIsInN1YiI6IjU5ODg2YTd' \
               'jOTI1MTQxM2Q0YTAzMTNmZCIsInNjb3BlcyI6Wy' \
               'JhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JF4fcJzt' \
               '-QpSf_Gu_x00huBN_TwU8NfVfxn5-x_V5NM'

SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
DISCOVER_MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"
MOVIE_TITLE = "Fight Club"
RELEASE_DATE = "2017-08-01"


def get_movie_id(movie_title):
    payload = {'api_key': API_KEY, 'query': movie_title}
    resp_dict = json.loads(requests.get(SEARCH_MOVIE_URL, headers={'Authorization': ACCESS_TOKEN}, params=payload).text)
    return resp_dict.get('results')[0].get('id')


def get_discovered_movies_as_dicts(release_date):
    # https://api.themoviedb.org/3/discover/movie?api_key=e2c84bd4529ef2b20608f45305fd3bc1&language=en-US&region=US&sort_by=popularity.desc&include_adult=true&page=1&release_date.gte=2017-08-01&with_release_type=4
    payload = {'api_key': API_KEY, 'language': 'en-US', 'region': 'US', 'include_adult': 'true', 'release_date.gte': release_date, 'with_release_type': 4}
    req = requests.get(DISCOVER_MOVIE_URL, headers={'Authorization': ACCESS_TOKEN}, params=payload)
    resp_dict = json.loads(req.text)
    return resp_dict


if __name__ == '__main__':
    print(get_discovered_movies_as_dicts(RELEASE_DATE))