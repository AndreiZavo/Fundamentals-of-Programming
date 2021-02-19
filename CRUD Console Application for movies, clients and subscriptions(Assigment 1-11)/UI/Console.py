import datetime

class Console(object):
    def __init__(self, movie_service, client_service, rental_service, undo):
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._undo = undo
        self._choices = {
            "1": self.ui_add_movie,
            "2": self.ui_remove_movie,
            "3": self.ui_update_movie,
            "4": self.ui_list_movies,
            "5": self.ui_add_client,
            "6": self.ui_remove_client,
            "7": self.ui_update_client,
            "8": self.ui_list_clients,
            "9": self.ui_rent,
            "10": self.ui_return,
            "r": self.ui_show_rentals,
            'sc': self.ui_search_client,
            'sm': self.ui_search_movie,
            'sr': self.ui_sort_rental,
            'u': self.ui_undo,
            't': self.ui_redo
        }

    @staticmethod
    def ui_choices():
        #ui menu for the user
        print("\nAssignment 11:")
        print("This are your options for the movie category:")
        print(" Press 1 to add a new movie           Press 2 to remove a movie")
        print(" Press 3 to update a movie            Press 4 to list the movies")
        print(" Press 5 to add a new client          Press 6 to remove a client")
        print(" Press 7 to update a client           Press 8 to list the clients")
        print(" Press 9 to create a rental           Press 10 to set a returned date for a movie")
        print(" Press sc to search for a client      Press sm to search for movies")
        print(" Press r to see the list of rentals   Press sr to see the top most")
        print("For undo press u and for redo press t")

    def ui_list_movies(self):
        #prints the list of movies
        movies = self._movie_service.get_movies()
        print('\n')
        for movie in movies:
            print(movie.__str__())

    def ui_add_movie(self):
        #takes an id, a title, a descrption and a genre and sends it to service in order to a new movie object be added
        id = input("Please insert an ID for movie: ")
        title = input("Please insert the title of movie: ")
        description = input("Please set a short description for the movie: ")
        genre = input("Please insert a genre for the movie: ")
        self._movie_service.add_movie(id, title, description, genre)

    def ui_remove_movie(self):
        #takes a title from the user in order to delete the movie corresponding with that specific title
        mv_id = input("Write the id of the movie you want to delete: ")
        self._movie_service.remove_movie(mv_id)

    def ui_update_movie(self):
        #prints a specific menu, and takes from the user a title to identify(in all cases) and new data to be inserted
        print("Please select one of the following according to your desire: ")
        print(" Press i if you want to update a id")
        print(" Press t if you want to update a title")
        print(" Press d if you want to update a description")
        print(" Press g if you want to update a genre")
        update_request = input("Type your choice: ")
        if update_request == 'i':
            id_to_find = input("Please type the id of the movie you want to change: ")
            new_id = input("Please type the new id: ")
            self._movie_service.update_movie_id(id_to_find, new_id)

        elif update_request == 't':
            id_to_found = input("Please type the id of the movie you want to change: ")
            new_title = input("Please type the new title: ")
            self._movie_service.update_movie_title(id_to_found, new_title)

        elif update_request == 'd':
            id_to_find = input("Please type the id of the movie you want to change: ")
            new_description = input("Please type the new description: ")
            self._movie_service.update_movie_description(id_to_find, new_description)

        elif update_request == 'g':
            id_to_find = input("Please type the id of the movie you want to change: ")
            new_genre = input("Please type the new genre: ")
            self._movie_service.update_movie_genre(id_to_find, new_genre)
        else:
            raise TypeError("Something went wrong! Please reenter data!")

    def ui_add_client(self):
        #takes from the user an id and a name and sends them to service to create a new client object and be added to list
        client_id = input("Write an ID for the client you want to insert: ")
        #validate_id
        client_name = input("Write a name for the client you want to insert: ")
        #validate_name
        self._client_service.add_client(client_id, client_name)

    def ui_list_clients(self):
        #prints the list of clients for the user
        clients = self._client_service.get_clients()
        print('\n')
        for client in clients:
            print(client.__str__())

    def ui_remove_client(self):
        #removes a client with a specific id
        id_of_client_to_remove = input("Write the ID of the client you want to remove: ")
        self._client_service.remove_client(id_of_client_to_remove)

    def ui_update_client(self):
        #prints a specific meniu, and takes from the user an id to identify(in all cases) and new data to be inserted
        print("Please select one of the following according to your desire: ")
        print(" Press i if you want to update a id")
        print(" Press n if you want to update a name")
        update_request = input("Type your choice: ")
        if update_request == 'i':
            id_to_find = input("Write the id of the client you want to change: ")
            new_id = input("Write the id you want to insert: ")
            self._client_service.update_client_id(id_to_find, new_id)
        elif update_request == 'n':
            id_to_find = input("Write the id of the client you want to change: ")
            new_name = input("Write the name you want to insert: ")
            self._client_service.update_client_name(id_to_find, new_name)

    def ui_rent(self):
        #creates a rental with coresponding filds
        rental_id = input("Please insert an id for the rental: ")
        movie_id = input("Please insert the id of the movie wanted to be rented: ")
        client_id = input("Please insert an client's id: ")
        rented_date = datetime.date.today().day
        a_week_for_rented_movie = 7
        limit_date = 24 #the limit date of month to return_the_same_month
        if rented_date > limit_date:
            due_date = rented_date - limit_date
        else:
            due_date = rented_date + a_week_for_rented_movie
        returned_date = "not returned"
        self._rental_service.add_rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)

    def ui_return(self):
        #adds a return date for a specific rental
        rental_id = input("Please insert the id of the rental for which you want to insert a returned date: ")
        returned_date = input("Insert the date of return for the rental #{}: ".format(rental_id))
        self._rental_service.set_returned_date(rental_id, returned_date)

    def ui_show_rentals(self):
        #prints the list of rentals
        rentals = self._rental_service.get_rentals()
        print('\n')
        for rental in rentals:
            print(rental.__str__())
        print('\n')

    def ui_search_client(self):
        #searches through the list of clients after id/name
        print("To search after id, press 1")
        print("To search after name, press 2")
        command = input(">>>  ")
        if command == '1':
            id_to_find = input("Please insert the client's id you want to see: ")
            client_to_show = self._client_service.search_for_client_by_id(id_to_find)
            print(client_to_show.__str__())
        if command == '2':
            name_to_find = input("Please insert the client's name you want to see: ")
            clients_found = []
            self._client_service.search_for_client_by_name(name_to_find, clients_found)
            print("The clients you are looking for are: \n")
            for clients in clients_found[0]:
                print(clients.__str__())

    def ui_search_movie(self):
        #searches through the list of movies after its fields
        movie = ['id', 'title', 'description', 'genre']
        for instruction in range(1, 5):
            print("To search after {}, press {}".format(movie[instruction - 1], instruction))
        command = input(">>> ")
        if command == '1':
            id_to_find = input("Please insert the movie's id you want to see: ")
            movie_to_show = self._movie_service.search_movie_by_id(id_to_find)
            print(movie_to_show.__str__())
        elif command == '2':
            title_to_find = input("Please insert the movie's title you want to see: ")
            movies_find = []
            self._movie_service.search_movie_by_title(title_to_find, movies_find)
            print("This are the movies matching your title: ")
            for movies in movies_find[0]:
                print(movies.__str__())
        elif command == '3':
            description_to_find = input("Please insert the movie's description you want to see: ")
            movies_find = []
            self._movie_service.search_movie_by_description(description_to_find, movies_find)
            print("This are the movies matching your description: ")
            for movies in movies_find[0]:
                print(movies.__str__())
        elif command == '4':
            genre_to_find = input("Please insert the movie's genre you want to see: ")
            movies_find = []
            self._movie_service.search_movie_by_genre(genre_to_find, movies_find)
            print("This are the movies matching your genre: ")
            for movies in movies_find[0]:
                print(movies.__str__())
        else:
            raise TypeError("Please insert a valid number!")

    def ui_sort_rental(self):
        #prints the top-most for different categories
        print("To see the list of most rented movies press 1")
        print("To see the list of most active clients press 2")
        print("To see the list of most overdue rentals press 3")
        command = input(">>>  ")
        if command == '1':
            movie_sorted_list = []
            self._rental_service.compute_list_of_rented_movies(movie_sorted_list)
            for movie in range(0, len(movie_sorted_list[0])):
                print("The movie with", '\033[1m', movie_sorted_list[0][movie][0], '\033[0m', "ID has been rented for ", movie_sorted_list[0][movie][1], "days")
        elif command == '2':
            client_sorted_list = []
            self._rental_service.compute_list_clients_id_with_total_days_of_rental(client_sorted_list)
            for client in range(0, len(client_sorted_list[0])):
                print("The client with ", '\033[1m', client_sorted_list[0][client][0], '\033[0m', "ID rented movies for ", client_sorted_list[0][client][1], "days")
        elif command == '3':
            late_rentals_list = []
            self._rental_service.compute_list_of_late_rentals(late_rentals_list)
            for rental in range(0, len(late_rentals_list[0])):
                if late_rentals_list[0][rental][1] == "not returned":
                    print("The rental with ", '\033[1m', late_rentals_list[0][rental][0], '\033[0m', "ID has not even been returned yet ")
                else:
                    print("The rental with ", '\033[1m', late_rentals_list[0][rental][0], '\033[0m', "ID has been rented for ", late_rentals_list[0][rental][1], "days")
        else:
            raise TypeError("The command you gave was incorrect. Please try again!")

    def ui_undo(self):
        self._undo.undo()

    def ui_redo(self):
        self._undo.redo()

    def ui_main(self):
        while True:
            self.ui_choices()
            index_of_command = input("Type the operation you want to pursue: ")
            if index_of_command == 'exit':
                return
            if index_of_command in self._choices:
                self._choices[index_of_command]()
            else:
                raise TypeError("Something went wrong! Please enter the number corresponding with the operation you desire")


