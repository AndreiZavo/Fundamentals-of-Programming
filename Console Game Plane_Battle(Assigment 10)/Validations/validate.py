from Exceptions.exception import Validation_Exception


class ValidateInputs(object):

    @staticmethod
    def validate_coordinates_of_player(raw, column):
        errors = ""
        if int(raw) not in range(1, 9):
            errors += "\nThe raw coordinate is not a number between 1 and 8"
        if int(column) not in range(1, 9):
            errors += "\nThe column coordinate is not a letter between a and h"
        if len(errors):
            raise Validation_Exception(errors)

    @staticmethod
    def validate_plane_of_player(board, raw, column):
        if board[raw][column] != '~':
            raise Validation_Exception("Please choose other coordinates for this plane. The planes should not overlap on the board")
