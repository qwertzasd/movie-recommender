import json
import requests

API_KEY = "e2c84bd4529ef2b20608f45305fd3bc1"
ACCESS_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' \
               '.eyJhdWQiOiJlMmM4NGJkNDUyOWVmMmIyMDYw' \
               'OGY0NTMwNWZkM2JjMSIsInN1YiI6IjU5ODg2YTd' \
               'jOTI1MTQxM2Q0YTAzMTNmZCIsInNjb3BlcyI6Wy' \
               'JhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JF4fcJzt' \
               '-QpSf_Gu_x00huBN_TwU8NfVfxn5-x_V5NM'
SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
DISCOVER_MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"
DESCRIBE_MOVIE_URL = "https://api.themoviedb.org/3/movie"
MOVIE_TITLE = "Fight Club"
RELEASE_DATE = "2017-08-30"
DEFAULT_PAYLOAD = {'api_key': API_KEY, 'language': 'en-US', 'region': 'US', 'include_adult': 'true',
                   'release_date.gte': RELEASE_DATE, 'with_release_type': 4, 'page': 1}


def get_movie_id(movie_title):
    payload = {'api_key': API_KEY, 'query': movie_title}
    resp_dict = get_response_text(SEARCH_MOVIE_URL, payload)
    return resp_dict.get('results')[0].get('id')


def get_discovered_movies(payload=DEFAULT_PAYLOAD):
    payload = dict(payload)

    resp_dict = get_response_text(DISCOVER_MOVIE_URL, payload)

    movies = resp_dict['results']
    total_page_num = resp_dict['total_pages']

    if total_page_num == payload['page']:
        return movies
    else:
        payload['page'] = payload['page'] + 1
        movies = movies + get_discovered_movies(payload)
    return movies


def get_movie_description(movie_id):
    payload = {'api_key': API_KEY}
    result = get_response_text(DESCRIBE_MOVIE_URL + "/" + str(movie_id), payload)
    return result


def get_response_text(url, payload):
    req = requests.get(url, headers={'Authorization': ACCESS_TOKEN}, params=payload)
    return json.loads(req.text)
