# media.py
# Author: Kevin Hutton
# Udacity Fullstack Developer Nanodegree Project 1
# August 2016


class Movie():
    """ Used to represent Movie Objects

        Attributes:
            title - The title of the movie
            storyline - Plot summary for the movie
            poster_image_url - URL pointing to poster image for the movie
            trailer_youtube_url - URL pointing to the trailer for the movie
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
