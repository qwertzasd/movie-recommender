# https://api.themoviedb.org/3/discover/movie?api_key=e2c84bd4529ef2b20608f45305fd3bc1&language=en-US&region=US&sort_by=popularity.desc&include_adult=true&page=1&release_date.gte=2017-08-01&with_release_type=4
# https://api.themoviedb.org/3/movie/550?api_key=e2c84bd4529ef2b20608f45305fd3bc1
from service.movie_recomennder_service import get_movies
from flask import Flask, jsonify, request, render_template, json
import time

from utility.MovieEncoder import MovieEncoder

app = Flask(__name__)

app.json_encoder = MovieEncoder
#locale.setlocale(locale.LC_ALL, 'de_DE')

@app.route("/getmovies", methods = ['POST', 'GET'])
def getmovies():
    print("running")
    # http://127.0.0.1:5000/getmovies?date=2017-09-05
    # date = request.args.get('date')
    # date = time.strftime("%Y-%m-%d") if request.args.get('date') is None

    date = request.form['date'] if request.method == 'POST' else None
    date = date if date is not None else time.strftime("%Y-%m-%d")
    print(date)
    movies = get_movies() if date is None else get_movies(date)
    # return jsonify(movies)
    movie_ = json.loads(json.dumps(movies))
    template = render_template('movies.html', movies=movie_)
    return template

@app.route("/getmoviesjson")
def getmoviesjson():
    print("running")
    # http://127.0.0.1:5000/getmoviesjson?date=2017-09-05
    date = request.args.get('date')
    print(date)
    # date = time.strftime("%Y-%m-%d") if request.args.get('date') is None
    date = date if date is not None else time.strftime("%Y-%m-%d")
    movies = get_movies() if date is None else get_movies(date)
    return jsonify(movies)

@app.route('/')
def index():
    return render_template('index.html')



app.run(threaded=True, debug=True)

# if __name__ == '__main__':
#     # description = get_movie_description(550)
#     # movies = get_discovered_movies()
#     # print(movies)
#     get_movies()
