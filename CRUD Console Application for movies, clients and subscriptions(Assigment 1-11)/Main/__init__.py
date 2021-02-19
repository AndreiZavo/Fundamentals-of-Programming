from Repository.repositories import *
from Service.services import *
from UI.Console import Console


def read_settings(filename, settings):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split("=")
                settings.append(parts[1].strip())


settings = list()
read_settings("settings.properties", settings)

undoStack = UndoStack()
redoStack = UndoStack()


if settings[0] == "inmemory":
    client_repository = Client_Repository()
    movie_repository = Movie_Repository()
    rental_repository = Rental_Repository()
    client_service = Client_Service(client_repository, undoStack, redoStack)
    movie_service = Movie_Service(movie_repository, undoStack, redoStack)
    rental_service = Rental_Service(movie_repository, client_repository, rental_repository)
elif settings[0] == "textfiles":
    client_repository = ClientFileRepository(settings[1], Client.read_client, Client.write_client)
    movie_repository = MovieFileRepository(settings[2], Movie.read_movie, Movie.write_movie)
    rental_repository = Rental_File_Repository(settings[3], Rental.read_rental, Rental.write_rental)
    client_service = FileServiceClients(client_repository, undoStack, redoStack)
    movie_service = MovieFileService(movie_repository, undoStack, redoStack)
    rental_service = Rental_Service(movie_repository, client_repository, rental_repository)
elif settings[0] == "binarryfiles":
    client_repository = BinaryRepositoryClients(settings[1], Client.read_client, Client.write_client)
    movie_repository = BinaryRepositoryMovie(settings[2], Movie.read_movie, Movie.write_movie)
    rental_repository = BinaryRepositoryRentals(settings[3], Rental.read_rental, Rental.write_rental)
    client_service = PickleClientService(client_repository, undoStack, redoStack)
    movie_service = PickleMovieService(movie_repository, undoStack, redoStack)
    rental_service = Rental_Service(movie_repository, client_repository, rental_repository)

service_undo = ServiceUndo(undoStack, redoStack)
ui = Console(movie_service, client_service, rental_service, service_undo)
ui.ui_main()




