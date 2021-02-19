import datetime

from Exceptions.erros import Valid_Exception


class Valid(object):

    @staticmethod
    def valid_movie(movie):
        errors = ""
        if int(movie.get_id()) < 100 or int(movie.get_id()) > 999:
            errors += "The id must be a 3-digit number!\n"
        if str(movie.get_title()) == "":
            errors += "No title has been inserted\n"
        if str(movie.get_description()) == "":
            errors += "No description has been inserted\n"
        if str(movie.get_genre()) == "":
            errors += "No genre has been inserted\n"
        if len(errors):
            raise Valid_Exception(errors)

    @staticmethod
    def validate_existence(list_of_movies, movie):
        for every_movie in list_of_movies:
            if str(movie.get_id()) == str(every_movie.get_id()):
                raise Valid_Exception("This movie already exists!")

    @staticmethod
    def valid_client(client):
        errors = ""
        if int(client.get_id()) < 10 or int(client.get_id()) > 99:
            errors += "The id must be a 2-digit number!\n"
        if str(client.get_name()) == "":
            errors += "No name has been inserted!\n"
        if len(errors):
            raise Valid_Exception(errors)

    @staticmethod
    def valid_existence_client(list_of_clients, client):
        for every_client in list_of_clients:
            if str(client.get_id()) == str(every_client.get_id()):
                raise Valid_Exception("This client_already exists!\n")

    @staticmethod
    def validate_rental(rental):
        errors = ""
        if int(rental.get_rental_id()) not in range(100, 999):
            errors += "The rental's ID must be a 3-digit number!\n"
        if int(rental.get_client_id()) < 10 or int(rental.get_client_id()) > 99:
            errors += "The client ID must be a 2-digit number!\n"
        if int(rental.get_movie_id()) not in range(100, 999):
            errors += "The movies ID must be a 3-digit number!\n"
        if str(rental.get_rented_date()) == "":
            errors += "No rented date has been inserted!\n"
        if len(errors):
            raise Valid_Exception(errors)

    @staticmethod
    def validate_existence_of_rental(rentals, rental):
        for every_rental in rentals:
            if int(every_rental.get_rental_id()) == int(rental.get_rental_id()):
                raise Valid_Exception("The rental already exists!")

    @staticmethod
    def existence_of_client_by_id(clients, client_id):
        id_found = False
        for every_client in clients:
            if every_client.get_id() == client_id:
                return
        if not id_found:
            raise Exception("There doesn't exist a client with this id!")

    @staticmethod
    def existence_of_movie_by_id(movies, movie_id):
        found = False
        for every_movie in movies:
            if str(every_movie.get_id()) == movie_id:
                return
        if not found:
            raise Exception("There doesn't exist a movie with this id!")

    @staticmethod
    def number_of_rentals_for_client_with_id(rental_repository, client_id):
        today = datetime.date.today().day
        rentals = rental_repository.get_rental_repository()
        for every_rental in rentals:
            if every_rental.get_client_id() == client_id:
                if int(every_rental.get_due_date()) > int(today):
                    raise Exception("This client has already rented at least one movie and haven't returned it yet!")
