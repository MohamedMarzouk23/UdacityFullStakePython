# -*- coding: utf-8 -*-
# By Mohamed Marzouk
# facebook.com/MohamedMarzouk23
import webbrowser
class Movie(object):
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)