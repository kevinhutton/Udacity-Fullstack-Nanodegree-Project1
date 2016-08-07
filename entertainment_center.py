# entertainment_center.py
# Author: Kevin Hutton
# Udacity Fullstack Developer Nanodegree Project 1
# August 2016

import media
import fresh_tomatoes

# Intialize Movie Objects which will be used to represent favorite movies
godfather = media.Movie(
    "The Godfather",
    "The patriarch of an organized crime dynasty transfers control of his\
     clandestine empire to his son",
    "https://i.ytimg.com/vi/rt-r-w7Z2Ag/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

star_wars = media.Movie(
    "Star Wars: Episode IV - A New Hope",
    "Luke Skywalker joins forces with a Jedi Knight, a pilot, a wookiee and two\
     droids to save the galaxy from the Empire's world-destroying\
     battle-station",
    "http://static7.comicvine.com/uploads/scale_super/0/40/4486147-star_wars_a_new_hope_ogn_cover.jpg",  # noqa
    "https://www.youtube.com/watch?v=vZ734NWnAHA")

signs = media.Movie(
    "Signs",
    "A family living on a farm finds mysterious crop circles in their fields\
     which suggests something more frightening to come",
    "http://ia.media-imdb.com/images/M/MV5BNDUwMDUyMDAyNF5BMl5BanBnXkFtZTYwMDQ3NzM3._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=F5-Lv4CJmFM")

batman_begins = media.Movie(
    "Batman Begins",
    "After training with his mentor, Batman begins his fight to free Gotham\
     City from Scarecrow and the League of Shadows",
    "http://vignette2.wikia.nocookie.net/batman/images/8/8d/Batman_Begins_poster1.jpg/revision/latest?cb=20111218141418",  # noqa
    "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

lotr_two_towers = media.Movie(
    "Lord of the Rings: The Two Towers",
    "The divided fellowship makes a stand against Sauron's new ally, Saruman,\
     and his hordes of Isengard",
    "http://ia.media-imdb.com/images/M/MV5BMTAyNDU0NjY4NTheQTJeQWpwZ15BbWU2MDk4MTY2Nw@@._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=cvCktPUwkW0")

# Place movie objects into single list so they can be placed on
# fresh_tomatoes.py generated html page
movies = [godfather, star_wars, signs, batman_begins, lotr_two_towers]

# Generate HTML page and populate with Movie objects
fresh_tomatoes.open_movies_page(movies)

