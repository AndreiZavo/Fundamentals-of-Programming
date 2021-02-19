class Client(object):

    def __init__(self, client_id, name):
        self._name = name
        self._id = client_id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_new_client(self, new_id, new_name):
        self._id = new_id
        self._name = new_name

    def __str__(self):
        return "ID: " + str(self.get_id()) + "\n Name: " + str(self.get_name())

    @staticmethod
    def read_client(line):
        parts = line.split(",")
        return Client(parts[0].strip(), parts[1].strip())

    @staticmethod
    def write_client(client):
        return str(client.get_id()) + "," + str(client.get_name())

class Movie(object):

    def __init__(self, movie_id, title, description, genre):
        self._genre = genre
        self._description = description
        self._title = title
        self._movie_id = movie_id

    def get_id(self):
        return self._movie_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_genre(self):
        return self._genre

    def set_new_movie(self, id, title, description, genre):
        self._movie_id = id
        self._title = title
        self._description = description
        self._genre = genre

    def __str__(self):
        return "\nMovie ID:  " + str(self.get_id()) + "\n     Title: " + str(self.get_title()) + "\nDescription:  " + str(self.get_description()) + "\nGenre : " + str(self.get_genre())

    @staticmethod
    def read_movie(line):
        parts = line.split(",")
        return Movie(parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip())

    @staticmethod
    def write_movie(movie):
        return str(movie.get_id()) + "," + str(movie.get_title()) + "," + str(movie.get_description()) + "," + str(movie.get_genre())


class Rental(object):
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        self._rental_id = rental_id
        self.__movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    def get_rental_id(self):
        #returns the string of reantal's id
        return str(self._rental_id)

    def get_rented_date(self):
        #returns the string of reantal's return date
        return str(self._rented_date)

    def get_due_date(self):
        #returns the string of reantal's due date
        return str(self._due_date)

    def set_return_date(self, new_returned_date):
        #sets the string of rental's returned date
        self._returned_date = new_returned_date

    def get_returned_date(self):
        #returns the string of rental's returned date
        return str(self._returned_date)

    def get_client_id(self):
        #returns the string of rental's client id
        return str(self._client_id)

    def get_movie_id(self):
        #returns the string of rental's movie id
        return str(self.__movie_id)

    def get_number_of_rented_days(self):
        if self._returned_date[0] == 'n':
            return_date = '23'
        elif self._returned_date[1] == '.':
            return_date = self._returned_date[0]
        else:
            return_date = self._returned_date[0] + self._returned_date[1]
        return int(return_date) - int(self._rented_date)

    def __str__(self):
        #returns an estetic print for a rental
        if str(self._returned_date)[0] == 'n':
            rental = "Rental ID: " + str(self._rental_id) + "\n  Client ID: " + str(self._client_id) + \
                     "\n  Movie ID: " + str(self.__movie_id) + "\n    Rented date: " + str(self._rented_date) + ".12.2019" \
                     + " \ " + '\033[1m' + " Due date: " + str(self._due_date)  + ".12.2019" \
                     +  '\033[0m' + " \ Returned date: " + str(self._returned_date) + '\n'
            return rental
        else:
            rental = "Rental ID: " + str(self._rental_id) + "\n  Client ID: " + str(self._client_id) + \
                     "\n  Movie ID: " + str(self.__movie_id) + "\n    Rented date: " + str(self._rented_date) + ".12.2019" \
                     + " \ " + '\033[1m' + " Due date: " + str(self._due_date) + ".12.2019" \
                     + '\033[0m' + " \ Returned date: " + str(self._returned_date) + "\n"
            return rental

    @staticmethod
    def read_rental(line):
        parts = line.split(",")
        return Rental(parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip(), parts[5].strip())

    @staticmethod
    def write_rental(rental):
        return str(rental.get_rental_id()) + "," + str(rental.get_movie_id()) + "," + str(rental.get_client_id()) + "," + str(rental.get_rented_date()) + "," + str(rental.get_due_date()) + "," + str(rental.get_returned_date())


class UndoAction(object):

    def __init__(self, repository, action, reverse_action, new_object, old_object):
        self.__repository = repository
        self.__action = action
        self.__reverse_action = reverse_action
        self.__new_object = new_object
        self.__old_object = old_object

    def get_repository(self):
        return self.__repository

    def get_action(self):
        return self.__action

    def get_reverse_action(self):
        return self.__reverse_action

    def get_new_object(self):
        return self.__new_object

    def get_old_object(self):
        return self.__old_object

    def execute(self):
        self.__action(self.__repository, self.__old_object)

    def execute_reverse_action(self):
        self.__action(self.__repository, self.__new_object)

    def get_opposite(self):
        return UndoAction(self.get_repository(), self.get_reverse_action(), self.get_action(), self.get_new_object(),
                          self.get_old_object())


class ComplexUndoAction(UndoAction):

    def __init__(self):
        self.__undo_actions = []

    def add_action(self, action):
        self.__undo_actions.append(action)

    def get_actions(self):
        return self.__undo_actions

    def execute(self):
        for index in range(len(self.__undo_actions) - 1, -1, -1):
            self.__undo_actions[index].execute()

    def get_opposite(self):
        opposite = ComplexUndoAction()
        for index in range(len(self.__undo_actions) - 1, -1, -1):
            action = self.__undo_actions[index]
            opposite.add_action(action.get_opposite())
        return opposite
