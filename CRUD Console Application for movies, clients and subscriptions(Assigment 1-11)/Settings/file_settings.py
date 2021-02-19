from Exceptions.erros import Settings_Exception


class Settings(object):

    def __init__(self):
        self._repository_type = '3'
        self.filename_movies = ""
        self.filename_clients = ""
        self.filename_rentals = ""

    def set_database(self, option):

        if option == '1':
            self.filename_movies = "movies.txt"
            self.filename_clients = "clients.txt"
            self.filename_rentals = "rentals.txt"
        elif option == '2':
            self.filename_movies = "pickle_movie.txt"
            self.filename_clients = "pickle_client.txt"
            self.filename_rentals = "pickle_rental.txt"
        else:
            raise Settings_Exception("Please insert a valid command!")
