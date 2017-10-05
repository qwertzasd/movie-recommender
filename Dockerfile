FROM ubuntu:16.04

MAINTAINER me

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev build-essential

RUN mkdir /tmp/movie-recommender

COPY ./requirements.txt /tmp/movie-recommender/requirements.txt

WORKDIR /tmp/movie-recommender

RUN pip install -r requirements.txt

ADD . /tmp/movie-recommender

#ENTRYPOINT [ "python" ]

#CMD [ "movie-recommender-app.py" ]
CMD [ "/bin/bash" ]
EXPOSE 5000