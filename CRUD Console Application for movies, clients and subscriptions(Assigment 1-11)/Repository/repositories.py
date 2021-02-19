import pickle
import random

from Domain.container import MyContainer
from Domain.enitties import Client, Movie, Rental
from Exceptions.erros import Repository_Exception
from Validation.validate import Valid


class Client_Repository(object):

    def __init__(self):
        self._clients = MyContainer()
        self.create_client()

    def get_all(self):
        return self._clients[:]

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
            client = Client(id, name)
            self.add_client(client)
            del probable_id[id_index]
            del probable_name[name_index]
            counter += 1

    def add_client(self, client):
        Valid.valid_client(client)
        Valid.valid_existence_client(self._clients, client)
        self._clients.append(client)

    def remove_client(self, client):
        Valid.valid_client(client)
        found = False
        for index in range(len(self._clients)):
            if str(self._clients[index].get_id()) == str(client.get_id()):
                del self._clients[index]
                return
        if not found:
            raise Repository_Exception("The movie you introduced doesn't exist")

    def update_client_id(self, client):
        Valid.valid_client(client)
        found = False
        for index in range(len(self._clients)):
            if str(self._clients[index].get_name()) == str(client.get_name()):
                self._clients[index].set_new_client(client.get_id(), client.get_name())
                return
        if not found:
            raise Repository_Exception("The client id you introduced doesn't exist")

    def update_client_name(self, client):
        Valid.valid_client(client)
        found = False
        for index in range(len(self._clients)):
            if str(self._clients[index].get_id()) == str(client.get_id()):
                self._clients[index].set_new_client(client.get_id(), client.get_name())
                return
        if not found:
            raise Repository_Exception("The client id you introduced doesn't exist")


class ClientFileRepository(Client_Repository):

    def __init__(self, filename, read_client, write_client):
        self._filename = filename
        self._read_object = read_client
        self._write_object = write_client
        Client_Repository.__init__(self)

    def _read_all_from_file(self):
        self._clients = []
        with open(self._filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entity = self._read_object(line)
                    self._clients.append(entity)

    def _write_all_to_file(self):
        with open(self._filename, 'w') as file:
            for entity in self._clients:
                line = self._write_object(entity)
                file.write(line + '\n')

    def add_client(self, client):
        self._read_all_from_file()
        Client_Repository.add_client(self, client)
        self._write_all_to_file()

    def get_all(self):
        self._read_all_from_file()
        return Client_Repository.get_all(self)

    def remove_client(self, client):
        self._read_all_from_file()
        Client_Repository.remove_client(self, client)
        self._write_all_to_file()

    def update_client_id(self, client):
        self._read_all_from_file()
        Client_Repository.update_client_id(self, client)
        self._write_all_to_file()

    def update_client_name(self, client):
        self._read_all_from_file()
        Client_Repository.update_client_name(self, client)
        self._write_all_to_file()


class BinaryRepositoryClients(Client_Repository):

    def __init__(self, filename, read_client, write_client):
        self.__filename = filename
        self._read_client = read_client
        self._write_client = write_client
        Client_Repository.__init__(self)

    def __write_binary_file(self):
        with open(self.__filename, "wb") as file:
            for client in self._clients:
                pickle.dump(self._write_client(client), file)

    def __read_binary_file(self):
        self._clients = []
        with open(self.__filename, "rb") as file:
            while True:
                try:
                    line = pickle.load(file)
                    student = self._read_client(line)
                    self._clients.append(student)
                except EOFError:
                    break

    def add_client(self, client):
        self.__read_binary_file()
        Client_Repository.add_client(self, client)
        self.__write_binary_file()

    def remove_client(self, client):
        self.__read_binary_file()
        Client_Repository.remove_client(self, client)
        self.__write_binary_file()

    def update_client_id(self, client):
        self.__read_binary_file()
        Client_Repository.update_client_id(self, client)
        self.__write_binary_file()

    def update_client_name(self, client):
        self.__read_binary_file()
        Client_Repository.update_client_name(self, client)
        self.__write_binary_file()

    def get_all(self):
        self.__read_binary_file()
        return Client_Repository.get_all(self)


class Movie_Repository(object):

    def __init__(self):
        self._movies = MyContainer()
        #self.create_movie()

    def get_all(self):
        return self._movies[:]

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
            self.add_movie(movie)
            del probable_id[id_index]
            del probable_title[movie_index]
            del probable_description[movie_index]
            del probable_genre[movie_index]
            counter += 1

    def add_movie(self, movie):
        Valid.valid_movie(movie)
        Valid.validate_existence(self._movies, movie)
        self._movies.append(movie)

    def remove_movie(self, movie):
        Valid.valid_movie(movie)
        found = False
        for index in range(len(self._movies)):
            if str(self._movies[index].get_id()) == str(movie.get_id()):
                del self._movies[index]
                return
        if not found:
            raise Repository_Exception("The movie you introduced doesn't exist")

    def update_movie_id(self, movie):
        Valid.valid_movie(movie)
        found = False
        for index in range(len(self._movies)):
            if str(self._movies[index].get_title()) == str(movie.get_title()):
                self._movies[index].set_new_movie(movie.get_id(), movie.get_title(), movie.get_description(), movie.get_genre())
                return
        if not found:
            raise Repository_Exception("The movie id you introduced doesn't exist")

    def update_movie(self, movie):
        Valid.valid_movie(movie)
        found = False
        for index in range(len(self._movies)):
            if str(self._movies[index].get_id()) == str(movie.get_id()):
                self._movies[index].set_new_movie(movie.get_id(), movie.get_title(), movie.get_description(), movie.get_genre())
                return
        if not found:
            raise Repository_Exception("The movie id you introduced doesn't exist")


class MovieFileRepository(Movie_Repository):

    def __init__(self, filename, read_object, write_object):
        self._filename = filename
        self._read_object = read_object
        self._write_object = write_object
        Movie_Repository.__init__(self)

    def _read_all_from_file(self):
        self._movies = []
        with open(self._filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entity = self._read_object(line)
                    self._movies.append(entity)

    def _write_all_to_file(self):
        with open(self._filename, 'w') as file:
            for entity in self._movies:
                line = self._write_object(entity)
                file.write(line + '\n')

    def add_movie(self, movie):
        self._read_all_from_file()
        Movie_Repository.add_movie(self, movie)
        self._write_all_to_file()

    def get_all(self):
        self._read_all_from_file()
        return Movie_Repository.get_all(self)

    def remove_movie(self, movie):
        self._read_all_from_file()
        Movie_Repository.remove_movie(self, movie)
        self._write_all_to_file()

    def update_movie_id(self, movie):
        self._read_all_from_file()
        Movie_Repository.update_movie_id(self, movie)
        self._write_all_to_file()

    def update_movie(self, movie):
        self._read_all_from_file()
        Movie_Repository.update_movie(self, movie)
        self._write_all_to_file()


class BinaryRepositoryMovie(Movie_Repository):

    def __init__(self, filename, read_movie, write_movie):
        self.__filename = filename
        self._read_movie = read_movie
        self._write_movie = write_movie
        Movie_Repository.__init__(self)

    def __write_binary_file(self):
        with open(self.__filename, "wb") as file:
            for student in self._movies:
                pickle.dump(self._write_movie(student), file)

    def __read_binary_file(self):
        self._movies = []
        with open(self.__filename, "rb") as file:
            while True:
                try:
                    line = pickle.load(file)
                    student = self._read_movie(line)
                    self._movies.append(student)
                except EOFError:
                    break

    def add_movie(self, movie):
        self.__read_binary_file()
        Movie_Repository.add_movie(self, movie)
        self.__write_binary_file()

    def remove_movie(self, movie):
        self.__read_binary_file()
        Movie_Repository.remove_movie(self, movie)
        self.__write_binary_file()

    def update_movie_id(self, movie):
        self.__read_binary_file()
        Movie_Repository.update_movie_id(self, movie)
        self.__write_binary_file()

    def update_movie(self, movie):
        self.__read_binary_file()
        Movie_Repository.update_movie(self, movie)
        self.__write_binary_file()

    def get_all(self):
        self.__read_binary_file()
        return Movie_Repository.get_all(self)


class Rental_Repository(object):

    def __init__(self):
        self._rentals = MyContainer()
        self.create_rental()

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
            self.add_rental(rental)
            del probable_rental_id[rental_id_index]
            del probable_client_id[client_id_index]
            del probable_movie_id[movie_id_index]
            counter += 1

    def get_all(self):
        return self._rentals[:]

    def add_rental(self, rental):
        Valid.validate_rental(rental)
        Valid.validate_existence_of_rental(self._rentals, rental)
        self._rentals.append(rental)

    def update_returned_date(self, rental):
        for every_rental in self._rentals:
            if str(every_rental.get_rental_id()) == str(rental.get_rental_id()):
                every_rental.set_return_date(rental.get_returned_date())
                return


class Rental_File_Repository(Rental_Repository):

    def __init__(self, filename, read_rental, write_rental):
        Rental_Repository.__init__(self)
        self._filename = filename
        self._read_rental = read_rental
        self._write_rental = write_rental

    def _read_all_to_file(self):
        self._rentals = []
        with open(self._filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                entity = self._read_rental(line)
                self._rentals.append(entity)

    def _write_all_from_file(self):
        with open(self._filename, 'w') as file:
            for entity in self._rentals:
                line = self._write_rental(entity)
                file.write(line + '\n')

    def get_all(self):
        self._read_all_to_file()
        return Rental_Repository.get_all(self)

    def add_rental(self, rental):
        self._read_all_to_file()
        Rental_Repository.add_rental(self, rental)
        self._write_all_from_file()

    def update_returned_date(self, rental):
        self._read_all_to_file()
        Rental_Repository.update_returned_date(self, rental)
        self._write_all_from_file()

class BinaryRepositoryRentals(Rental_Repository):

    def __init__(self, filename, read_rental, write_rental):
        self.__filename = filename
        self._read_rental = read_rental
        self._write_rental = write_rental
        Rental_Repository.__init__(self)

    def __write_binary_file(self):
        with open(self.__filename, "wb") as file:
            for rental in self._rentals:
                pickle.dump(self._write_rental(rental), file)

    def __read_binary_file(self):
        self._rentals = []
        with open(self.__filename, "rb") as file:
            while True:
                try:
                    line = pickle.load(file)
                    student = self._read_rental(line)
                    self._rentals.append(student)
                except EOFError:
                    break

    def add_rental(self, rental):
        self.__read_binary_file()
        Rental_Repository.add_rental(self, rental)
        self.__write_binary_file()

    def update_returned_date(self, rental):
        self.__read_binary_file()
        Rental_Repository.update_returned_date(self, rental)
        self.__write_binary_file()

    def get_all(self):
        self.__read_binary_file()
        return Rental_Repository.get_all(self)


class UndoStack(object):

    def __init__(self):
        self.__undo_actions = []

    def push(self, action):
        self.__undo_actions.append(action)
        #print(self.__undo_actions)

    def pop(self):
        if len(self.__undo_actions) == 0:
            raise Exception("No more actions!")
        return self.__undo_actions.pop()

    def clear(self):
        self.__undo_actions = []
