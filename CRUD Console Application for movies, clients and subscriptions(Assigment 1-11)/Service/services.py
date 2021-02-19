from fuzzywuzzy import fuzz

from Domain.enitties import UndoAction, Rental
from Exceptions.erros import Service_Exception
from Repository.repositories import *
from Validation.validate import Valid


class Client_Service(object):

    def __init__(self, client_repository, undostack, redostack):
        self._redostack = redostack
        self._undostack = undostack
        self._client_repository = client_repository

    def get_clients(self):
        return self._client_repository.get_all()

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self._client_repository.add_client(client)
        action = UndoAction(self._client_repository, Client_Repository.remove_client, Client_Repository.add_client,
                            client, client)
        self._undostack.push(action)
        self._redostack.clear()

    def remove_client(self, id_delete):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == id_delete:
                client_to_delete = Client(id_delete, every_client.get_name())
                self._client_repository.remove_client(client_to_delete)
                action = UndoAction(self._client_repository, Client_Repository.add_client,
                                    Client_Repository.remove_client, client_to_delete, client_to_delete)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_client_id(self, old_client_id, new_client_id):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(new_client_id, every_client.get_name())
                self._client_repository.update_client_id(client_to_update)
                action = UndoAction(self._client_repository, Client_Repository.update_client_id,
                                    Client_Repository.update_client_id, client_to_update, old_client)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_client_name(self, old_client_id, new_client_name):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(every_client.get_id(), new_client_name)
                self._client_repository.update_client_name(client_to_update)
                action = UndoAction(self._client_repository, Client_Repository.update_client_name,
                                    Client_Repository.update_client_name, client_to_update, old_client)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def search_for_client_by_id(self, id_to_find):
        found = False
        for client in self._client_repository.get_all():
            similarity_percent = fuzz.token_set_ratio(str(client.get_id()), id_to_find)
            if similarity_percent > 50:
                return client
        if not found:
            raise Service_Exception("It doesn't exist a client with this id!")

    def search_for_client_by_name(self, name_to_find, list_to_show):
        found = False
        clients_to_return = Client_Repository()
        for client in self.get_clients():
            similarity_percent = fuzz.token_set_ratio(str(client.get_name()), name_to_find)
            if similarity_percent > 40:
                clients_to_return.add_client(client)
                found = True
        if not found:
            raise Service_Exception("It doesn't exist a client with this name!")
        else:
            list_to_show.append(clients_to_return._clients)


class FileServiceClients(object):

    def __init__(self, repository_clients, undo_stack, redo_stack):
        self._client_repository = repository_clients
        self._undo_stack = undo_stack
        self._redo_stack = redo_stack

    def get_clients(self):
        return self._client_repository.get_all()

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self._client_repository.add_client(client)
        action = UndoAction(self._client_repository, ClientFileRepository.remove_client,
                            ClientFileRepository.add_client,
                            client, client)
        self._undo_stack.push(action)
        self._redo_stack.clear()

    def remove_client(self, id_delete):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == id_delete:
                client_to_delete = Client(id_delete, every_client.get_name())
                self._client_repository.remove_client(client_to_delete)
                action = UndoAction(self._client_repository, ClientFileRepository.add_client,
                                    ClientFileRepository.remove_client,
                                    client_to_delete, client_to_delete)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_client_id(self, old_client_id, new_client_id):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(new_client_id, every_client.get_name())
                self._client_repository.update_client_id(client_to_update)
                action = UndoAction(self._client_repository, ClientFileRepository.update_client_id,
                                    ClientFileRepository.update_client_id, client_to_update, old_client)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_client_name(self, old_client_id, new_client_name):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(every_client.get_id(), new_client_name)
                self._client_repository.update_client_name(client_to_update)
                action = UndoAction(self._client_repository, ClientFileRepository.update_client_name,
                                    ClientFileRepository.update_client_name, client_to_update, old_client)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return


class PickleClientService(object):

    def __init__(self, client_repository, undo_stack, redo_stack):
        self._client_repository = client_repository
        self._undo_stack = undo_stack
        self._redo_stack = redo_stack

    def get_clients(self):
        return self._client_repository.get_all()

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self._client_repository.add_client(client)
        action = UndoAction(self._client_repository, BinaryRepositoryClients.remove_client,
                            BinaryRepositoryClients.add_client,
                            client, client)
        self._undo_stack.push(action)
        self._redo_stack.clear()

    def remove_client(self, id_delete):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == id_delete:
                client_to_delete = Client(id_delete, every_client.get_name())
                self._client_repository.remove_client(client_to_delete)
                action = UndoAction(self._client_repository, BinaryRepositoryClients.add_client,
                                    BinaryRepositoryClients.remove_client,
                                    client_to_delete, client_to_delete)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_client_id(self, old_client_id, new_client_id):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(new_client_id, every_client.get_name())
                self._client_repository.update_client_id(client_to_update)
                action = UndoAction(self._client_repository, BinaryRepositoryClients.update_client_id,
                                    BinaryRepositoryClients.update_client_id, client_to_update, old_client)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_client_name(self, old_client_id, new_client_name):
        for every_client in self._client_repository.get_all():
            if str(every_client.get_id()) == old_client_id:
                old_client = every_client
                client_to_update = Client(every_client.get_id(), new_client_name)
                self._client_repository.update_client_name(client_to_update)
                action = UndoAction(self._client_repository, BinaryRepositoryClients.update_client_name,
                                    BinaryRepositoryClients.update_client_name, client_to_update, old_client)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return


class Movie_Service(object):

    def __init__(self, movie_repository, undostack, redostack):
        self._movie_repository = movie_repository
        self._undostack = undostack
        self._redostack = redostack

    def get_movies(self):
        return self._movie_repository.get_all()

    def add_movie(self, movie_id, title, description, genre):
        movie = Movie(movie_id, title, description, genre)
        self._movie_repository.add_movie(movie)
        action = UndoAction(self._movie_repository, Movie_Repository.remove_movie, Movie_Repository.add_movie, movie,
                            movie)
        self._undostack.push(action)
        self._redostack.clear()

    def remove_movie(self, id_delete):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == id_delete:
                movie_to_delete = Movie(id_delete, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.remove_movie(movie_to_delete)
                action = UndoAction(self._movie_repository, Movie_Repository.add_movie, Movie_Repository.remove_movie,
                                    movie_to_delete, movie_to_delete)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_id(self, old_movie_id, new_movie_id):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(new_movie_id, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie_id(movie_to_update)
                action = UndoAction(self._movie_repository, Movie_Repository.update_movie_id,
                                    Movie_Repository.update_movie_id,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_title(self, old_movie_id, new_movie_title):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), new_movie_title, every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, Movie_Repository.update_movie, Movie_Repository.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_description(self, old_movie_id, new_movie_description):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), new_movie_description,
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, Movie_Repository.update_movie, Movie_Repository.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_genre(self, old_movie_id, new_movie_genre):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), every_movie.get_description(),
                                        new_movie_genre)
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, Movie_Repository.update_movie, Movie_Repository.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def search_movie_by_id(self, id_to_find):
        found = False
        for movie in self.get_movies():
            similarity_percent = fuzz.token_set_ratio(str(movie.get_id()), id_to_find)
            if similarity_percent > 50:
                return movie
        if not found:
            raise Service_Exception("This movie doesn't exist in list!")

    def search_movie_by_title(self, title_to_find, list_to_show):
        found = False
        movies = Movie_Repository()
        for movie in self.get_movies():
            similarity_percent = fuzz.token_set_ratio(str(movie.get_title()), title_to_find)
            if similarity_percent > 40:
                movies.add_movie(movie)
                found = True
        if not found:
            raise Service_Exception("This movie doesn't exist in list!")
        else:
            list_to_show.append(movies.get_all())

    def search_movie_by_description(self, description_to_find, list_to_show):
        found = False
        movies = Movie_Repository()
        for movie in self.get_movies():
            similarity_percent = fuzz.token_set_ratio(str(movie.get_description()), description_to_find)
            if similarity_percent > 20:
                movies.add_movie(movie)
                found = True
        if not found:
            raise Service_Exception("This movie doesn't exist in list!")
        else:
            list_to_show.append(movies.get_all())

    def search_movie_by_genre(self, genre_to_find, list_to_show):
        found = False
        movies = Movie_Repository()
        for movie in self.get_movies():
            similarity_percent = fuzz.token_set_ratio(str(movie.get_genre()), genre_to_find)
            if similarity_percent > 50:
                movies.add_movie(movie)
                found = True
        if not found:
            raise Service_Exception("This movie doesn't exist in list!")
        else:
            list_to_show.append(movies.get_all())


class MovieFileService(object):

    def __init__(self, movie_repository, undo_stack, redo_stack):
        self._movie_repository = movie_repository
        self._undo_stack = undo_stack
        self._redo_stack = redo_stack

    def get_movies(self):
        return self._movie_repository.get_all()

    def add_movie(self, movie_id, title, description, genre):
        movie = Movie(movie_id, title, description, genre)
        self._movie_repository.add_movie(movie)
        action = UndoAction(self._movie_repository, MovieFileRepository.remove_movie, MovieFileRepository.add_movie,
                            movie,
                            movie)
        self._undo_stack.push(action)
        self._redo_stack.clear()

    def remove_movie(self, id_delete):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == id_delete:
                movie_to_delete = Movie(id_delete, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.remove_movie(movie_to_delete)
                action = UndoAction(self._movie_repository, MovieFileRepository.add_movie, MovieFileRepository.remove_movie,
                                    movie_to_delete, movie_to_delete)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_movie_id(self, old_movie_id, new_movie_id):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(new_movie_id, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie_id(movie_to_update)
                action = UndoAction(self._movie_repository, MovieFileRepository.update_movie_id,
                                    MovieFileRepository.update_movie_id,
                                    movie_to_update, old_movie)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_movie_title(self, old_movie_id, new_movie_title):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), new_movie_title, every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, MovieFileRepository.update_movie,
                                    MovieFileRepository.update_movie,
                                    movie_to_update, old_movie)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_movie_description(self, old_movie_id, new_movie_description):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), new_movie_description,
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, MovieFileRepository.update_movie,
                                    MovieFileRepository.update_movie,
                                    movie_to_update, old_movie)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return

    def update_movie_genre(self, old_movie_id, new_movie_genre):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), every_movie.get_description(),
                                        new_movie_genre)
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, MovieFileRepository.update_movie,
                                    MovieFileRepository.update_movie,
                                    movie_to_update, old_movie)
                self._undo_stack.push(action)
                self._redo_stack.clear()
                return


class PickleMovieService(object):

    def __init__(self, movie_repository, undostack, redostack):
        self._movie_repository = movie_repository
        self._undostack = undostack
        self._redostack = redostack

    def get_movies(self):
        return self._movie_repository.get_all()

    def add_movie(self, movie_id, title, description, genre):
        movie = Movie(movie_id, title, description, genre)
        self._movie_repository.add_movie(movie)
        action = UndoAction(self._movie_repository, BinaryRepositoryMovie.remove_movie, BinaryRepositoryMovie.add_movie,
                            movie,
                            movie)
        self._undostack.push(action)
        self._redostack.clear()

    def remove_movie(self, id_delete):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == id_delete:
                movie_to_delete = Movie(id_delete, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.remove_movie(movie_to_delete)
                action = UndoAction(self._movie_repository, BinaryRepositoryMovie.add_movie, BinaryRepositoryMovie.remove_movie,
                                    movie_to_delete, movie_to_delete)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_id(self, old_movie_id, new_movie_id):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(new_movie_id, every_movie.get_title(), every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie_id(movie_to_update)
                action = UndoAction(self._movie_repository, BinaryRepositoryMovie.update_movie_id,
                                    BinaryRepositoryMovie.update_movie_id,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_title(self, old_movie_id, new_movie_title):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), new_movie_title, every_movie.get_description(),
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, BinaryRepositoryMovie.update_movie,
                                    BinaryRepositoryMovie.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return
    def update_movie_description(self, old_movie_id, new_movie_description):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), new_movie_description,
                                        every_movie.get_genre())
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, BinaryRepositoryMovie.update_movie,
                                    BinaryRepositoryMovie.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

    def update_movie_genre(self, old_movie_id, new_movie_genre):
        for every_movie in self._movie_repository.get_all():
            if str(every_movie.get_id()) == old_movie_id:
                old_movie = every_movie
                movie_to_update = Movie(every_movie.get_id(), every_movie.get_title(), every_movie.get_description(),
                                        new_movie_genre)
                self._movie_repository.update_movie(movie_to_update)
                action = UndoAction(self._movie_repository, BinaryRepositoryMovie.update_movie,
                                    BinaryRepositoryMovie.update_movie,
                                    movie_to_update, old_movie)
                self._undostack.push(action)
                self._redostack.clear()
                return

class Rental_Service(object):

    def __init__(self, movie_repository, client_repository, rental_repository):
        self._movie_repository = movie_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository

    def get_rentals(self):
        return self._rental_repository.get_all()

    def add_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        Valid.existence_of_client_by_id(self._client_repository.get_all(), client_id)
        Valid.existence_of_movie_by_id(self._movie_repository.get_all(), movie_id)
        self._rental_repository.add_rental(rental)

    def set_returned_date(self, rental_id, returned_date):
        for rental in self._rental_repository.get_all():
            if str(rental.get_rental_id()) == rental_id:
                rental_update = Rental(rental.get_rental_id(), rental.get_movie_id(), rental.get_client_id(),
                                       rental.get_rented_date(), rental.get_due_date(), returned_date)
                self._rental_repository.update_returned_date(rental_update)

    def compute_list_movies_id_with_days_of_rent(self):
        # computes a list of most rented movies ordered in a descending order
        client_repository = Client_Repository()
        movie_repository = Movie_Repository()
        sort_rental_list = Rental_Repository()
        sort_rental_list._rental_repository = self.get_rentals()
        for step_i in range(0, len(sort_rental_list.get_all()) - 1):
            for step_j in range(step_i + 1, len(sort_rental_list.get_all())):
                if sort_rental_list._rental_repository[step_i].get_number_of_rented_days() < \
                        sort_rental_list._rental_repository[step_j].get_number_of_rented_days():
                    aux = sort_rental_list._rental_repository[step_i]
                    sort_rental_list._rental_repository[step_i] = sort_rental_list._rental_repository[step_j]
                    sort_rental_list._rental_repository[step_j] = aux
        list_of_movies_id = []
        for rental in sort_rental_list.get_all():
            list_of_movies_id.append([rental.get_movie_id(), rental.get_number_of_rented_days()])
        return list_of_movies_id

    def compute_list_of_rented_movies(self, movie_list):
        # adds the list as a first element if the list for the top most rented movies
        list_of_movies = self.compute_list_movies_id_with_days_of_rent()
        movie_list.append(list_of_movies)

    def days_of_rented_movies(self, client_id):
        # returns the number of days of rented movies
        days_of_rent = 0
        for rental in self._rental_repository.get_all():
            if rental.get_client_id() == client_id:
                days_of_rent += rental.get_number_of_rented_days()
        return days_of_rent

    def compute_list_clients_id_with_total_days_of_rental(self, client_list):
        # creates a list for top most active clients regarding the number of days of renting movies and adds it to a list set as parameter
        list_of_most_active_clients = []
        for rent in self._rental_repository.get_all():
            list_of_most_active_clients.append(
                [rent.get_client_id(), self.days_of_rented_movies(rent.get_client_id())])
        for step_i in range(0, len(list_of_most_active_clients) - 1):
            for step_j in range(step_i, len(list_of_most_active_clients)):
                if list_of_most_active_clients[step_i][1] < list_of_most_active_clients[step_j][1]:
                    aux = list_of_most_active_clients[step_i]
                    list_of_most_active_clients[step_i] = list_of_most_active_clients[step_j]
                    list_of_most_active_clients[step_j] = aux
        client_list.append(list_of_most_active_clients)

    def compute_list_of_late_rentals(self, late_rentals_list):
        # creates a list for top most overdue rentals and adds it to a list set as parameter
        rentals_overdue = []
        not_returned_movies = []
        position = 0
        for rental in self._rental_repository.get_all():
            if rental.get_returned_date() == "not returned":
                not_returned_movies.append(position)
                rentals_overdue.append([rental.get_rental_id(), rental.get_returned_date()])
            else:
                rentals_overdue.append([rental.get_rental_id(), rental.get_number_of_rented_days()])
            position += 1
        cursor = 0
        while cursor < len(not_returned_movies):
            rentals_overdue.insert(cursor, rentals_overdue[not_returned_movies[cursor]])
            del rentals_overdue[not_returned_movies[cursor] + 1]
            cursor += 1
        for step_i in range(len(not_returned_movies), len(rentals_overdue) - 1):
            for step_j in range(step_i, len(rentals_overdue)):
                if rentals_overdue[step_i][1] < rentals_overdue[step_j][1]:
                    aux = rentals_overdue[step_i]
                    rentals_overdue[step_i] = rentals_overdue[step_j]
                    rentals_overdue[step_j] = aux
        late_rentals_list.append(rentals_overdue)

class PickleRentalService(object):

    def __init__(self, rental_repository, undo_stack, redo_stack):
        self._rental_repository = rental_repository
        self._undo_stack = undo_stack
        self._redo_stack = redo_stack

    def get_rentals(self):
        return self._rental_repository.get_all()

    def add_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        Valid.existence_of_client_by_id(self._client_repository.get_all(), client_id)
        Valid.existence_of_movie_by_id(self._movie_repository.get_all(), movie_id)
        self._rental_repository.add_rental(rental)

    def set_returned_date(self, rental_id, returned_date):
        for rental in self._rental_repository.get_all():
            if str(rental.get_rental_id()) == rental_id:
                rental_update = Rental(rental.get_rental_id(), rental.get_movie_id(), rental.get_client_id(),
                                       rental.get_rented_date(), rental.get_due_date(), returned_date)
                self._rental_repository.update_returned_date(rental_update)

    def repository_compute_list_movies_id_with_days_of_rent(self):
        # computes a list of most rented movies ordered in a descending order
        client_repository = Client_Repository()
        movie_repository = Movie_Repository()
        sort_rental_list = Rental_Repository()
        sort_rental_list._rental_repository = self.get_rentals()
        for step_i in range(0, len(sort_rental_list.get_rental_repository()) - 1):
            for step_j in range(step_i + 1, len(sort_rental_list.get_rental_repository())):
                if sort_rental_list._rental_repository[step_i].get_number_of_rented_days() < \
                        sort_rental_list._rental_repository[step_j].get_number_of_rented_days():
                    aux = sort_rental_list._rental_repository[step_i]
                    sort_rental_list._rental_repository[step_i] = sort_rental_list._rental_repository[step_j]
                    sort_rental_list._rental_repository[step_j] = aux
        list_of_movies_id = []
        for rental in sort_rental_list.get_rental_repository():
            list_of_movies_id.append([rental.get_movie_id(), rental.get_number_of_rented_days()])
        return list_of_movies_id

    def repository_compute_list_of_rented_movies(self, movie_list):
        # adds the list as a first element if the list for the top most rented movies
        list_of_movies = self.repository_compute_list_movies_id_with_days_of_rent()
        movie_list.append(list_of_movies)

    def repository_days_of_rented_movies(self, client_id):
        # returns the number of days of rented movies
        days_of_rent = 0
        for rental in self.get_rental_repository():
            if rental.get_client_id() == client_id:
                days_of_rent += rental.get_number_of_rented_days()
        return days_of_rent

    def repository_compute_list_clients_id_with_total_days_of_rental(self, client_list):
        # creates a list for top most active clients regarding the number of days of renting movies and adds it to a list set as parameter
        list_of_most_active_clients = []
        for rent in self.get_rental_repository():
            list_of_most_active_clients.append(
                [rent.get_client_id(), self.repository_days_of_rented_movies(rent.get_client_id())])
        for step_i in range(0, len(list_of_most_active_clients) - 1):
            for step_j in range(step_i, len(list_of_most_active_clients)):
                if list_of_most_active_clients[step_i][1] < list_of_most_active_clients[step_j][1]:
                    aux = list_of_most_active_clients[step_i]
                    list_of_most_active_clients[step_i] = list_of_most_active_clients[step_j]
                    list_of_most_active_clients[step_j] = aux
        client_list.append(list_of_most_active_clients)

    def repository_compute_list_of_late_rentals(self, late_rentals_list):
        # creates a list for top most overdue rentals and adds it to a list set as parameter
        rentals_overdue = []
        not_returned_movies = []
        position = 0
        for rental in self.get_rental_repository():
            if rental.get_returned_date() == "not returned":
                not_returned_movies.append(position)
                rentals_overdue.append([rental.get_rental_id(), rental.get_returned_date()])
            else:
                rentals_overdue.append([rental.get_rental_id(), rental.get_number_of_rented_days()])
            position += 1
        cursor = 0
        while cursor < len(not_returned_movies):
            rentals_overdue.insert(cursor, rentals_overdue[not_returned_movies[cursor]])
            del rentals_overdue[not_returned_movies[cursor] + 1]
            cursor += 1
        for step_i in range(len(not_returned_movies), len(rentals_overdue) - 1):
            for step_j in range(step_i, len(rentals_overdue)):
                if rentals_overdue[step_i][1] < rentals_overdue[step_j][1]:
                    aux = rentals_overdue[step_i]
                    rentals_overdue[step_i] = rentals_overdue[step_j]
                    rentals_overdue[step_j] = aux
        late_rentals_list.append(rentals_overdue)

class ServiceUndo(object):

    def __init__(self, undoStack, redoStack):
        self.__undoStack = undoStack
        self.__redoStack = redoStack

    def undo(self):
        action = self.__undoStack.pop()
        action.execute()
        redo_action = action.get_opposite()
        self.__redoStack.push(redo_action)

    def redo(self):
        action = self.__redoStack.pop()
        action.execute_reverse_action()
        redo_action = action.get_opposite()
        self.__undoStack.push(redo_action)
