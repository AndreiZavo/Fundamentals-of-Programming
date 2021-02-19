from Domain.client import Client
from Domain.movie import Movie
import random

class Initialization:

    def __init__(self, movie_repository, client_repository):
        self._movie_repository = movie_repository
        self._client_repository = client_repository
        #self._rental_repository = rental_repository

    def create_movie(self):
        #initialize list of movies with 10 exemples
        probable_id = list(range(101, 999))
        probable_title = [
            'Good Will Hunting',
            'Inception',
            'Prestige',
            'Fight Club',
            'Coach Carter',
            'The Shawshank Redemption',
            'Forest Gump',
            'The Silence of the Lambs',
            'Star Wars',
            'Interstellar'
        ]
        probable_description = [
            'A boy from the geto, who is good at math',
            'A dream in a dream in a dream',
            'A movie with two magicians',
            'We do not talk about this movie',
            'Samuel L.Jackson is a basketball-coach nothing to be add',
            'Two imprisoned men bond and help each other to redeam themselfs',
            'Unfold through the perspective of a man with an IQ of 75',
            'Best detective vs.criminal story ever',
            'Space-ships and The FORCE are in this movie',
            'A 3 hour movie with Matthew McConaughey'
        ]
        probable_genre = [
            'Drama',
            'Action - Drama',
            'Drama-Fantasy',
            'Action - Drama',
            'Drama - Sport',
            'Drama',
            'Drama-Romance',
            'Crime-Thriller',
            'Adventure-Fantasy',
            'Sci-Fi'
        ]
        counter = 0
        while counter < 10:
            id_index = random.randrange(len(probable_id))
            id = probable_id[id_index]
            movie_index = random.randrange(len(probable_title))
            title = probable_title[movie_index]
            description = probable_description[movie_index]
            genre = probable_genre[movie_index]
            movie = Movie(id, title, description, genre)
            self._movie_repository.add_movie(movie)
            del probable_id[id_index]
            del probable_title[movie_index]
            del probable_description[movie_index]
            del probable_genre[movie_index]
            counter += 1

    def create_client(self):
        #initialize list of clients with 10 exemples
        probable_id = list(range(10,99))
        probable_name = [
            'Suzanne Daye',
            'Eldridge Laubscher',
            'Kati Riss',
            'Vickie Morant',
            'Lissette Mcbryde',
            'Charla Dane',
            'Emanuel Burrell',
            'Markita Bonds',
            'Diann Mechem',
            'Lauryn Barkley'
        ]
        counter = 0
        while counter < 10:
            id_index = random.randrange(len(probable_id))
            id = probable_id[id_index]
            name_index = random.randrange(len(probable_name))
            name = probable_name[name_index]
            client = Client(id,name)
            self._client_repository.add_client(client)
            del probable_id[id_index]
            del probable_name[name_index]
            counter += 1

    def create_rental(self):
        #initialize list of rentals with 3 examples
        probable_movie_id = list(range(100, 999))
        probable_client_id = list(range(10,99))
        probable_rent_date = list(range(7,24))
        probable_rental_id = list(range(100, 999))
        counter = 0
        days_of_rental = 7
        while counter < 3:
            rental_id_index = random.randrange(len(probable_rental_id))
            rental_id = probable_rental_id[rental_id_index]
            movie_id_index = random.randrange(len(probable_movie_id))
            movie_id = probable_movie_id[movie_id_index]
            client_id_index = random.randrange(len(probable_client_id))
            client_id = probable_client_id[client_id_index]
            rent_date_index = random.randrange(len(probable_rent_date))
            rent_date = probable_rent_date[rent_date_index]
            due_date = rent_date + days_of_rental
            return_date = str(rent_date + random.randrange(0, 10)) + ".12.2019"
            rental = Rental(rental_id, movie_id, client_id, rent_date, due_date, return_date)
            self._rental_repository.repository_add_rental(rental)
            del probable_rental_id[rental_id_index]
            del probable_client_id[client_id_index]
            del probable_movie_id[movie_id_index]
            counter += 1
