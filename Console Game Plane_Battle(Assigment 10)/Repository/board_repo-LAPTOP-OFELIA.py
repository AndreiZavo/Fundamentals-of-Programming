import random
import sys

sys.setrecursionlimit(3500)

class BoardToAttack(object):

    def __init__(self):
        self._mirror_board = []
        self.create_board(self._mirror_board)
        self._board = []
        self.create_board(self._board)
        scenarios = {
            '1': self.create_scenario_1,
            '2': self.create_scenario_2,
            '3': self.create_scenario_3,
            '4': self.create_scenario_4,
            '5': self.create_scenario_5
        }
        random_scenario = random.randrange(1, 6)
        scenarios[str(random_scenario)]()

    @staticmethod
    def create_board(board):
        character_line = ['/', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for line in range(0, 9):
            board.append(["~"] * 9)
        for column in range(0, 9):
            board[0][column] = character_line[column]
        for line in range(1, 9):
            board[line][0] = str(line)

    def create_scenario_1(self):
        #first plane
        self._board[7][3] = 'ᐁ' #cabin
        for box in range(1, 6):
            self._board[6][box] = '▧' #wings
        self._board[5][3] = '▧' #middle
        for box in range(2, 5):
            self._board[4][box] = '▧' #tail
        #second plane
        self._board[3][8] = 'ᐅ' #cabin
        for box in range(1, 6):
            self._board[box][7] = '▣' #wings
        self._board[3][6] = '▣' #middle
        for box in range(2, 5):
            self._board[box][5] = '▣' #tail

    def create_scenario_2(self):
        #first plane
        self._board[5][1] = 'ᐊ' #cabin
        for box in range(3, 8):
            self._board[box][2] = '◼' #wings
        self._board[5][3] = '◼' #middle
        for box in range(4, 7):
            self._board[box][4] = '◼' #tail
        #second plane
        self._board[1][6] = 'ᐃ' #cabin
        for box in range(4, 9):
            self._board[2][box] = '◍' #wings
        self._board[3][6] = '◍' #middle
        for box in range(5, 8):
            self._board[4][box] = '◍' #tail

    def create_scenario_3(self):
        #first plane
        self._board[6][5] = 'ᐁ' #cabin
        for box in range(3, 8):
            self._board[5][box] = '▧' #wings
        self._board[4][5] = '▧' #middle
        for box in range(4, 7):
            self._board[3][box] = '▧' #tail
        #second plane
        self._board[1][3] = 'ᐃ' #cabin
        for box in range(1, 6):
            self._board[2][box] = '◍' #wings
        self._board[3][3] = '◍' #middle
        for box in range(2, 5):
            self._board[4][box] = '◍' #tail

    def create_scenario_4(self):
        #first plane
        self._board[4][6] = 'ᐁ' #cabin
        for box in range(4, 9):
            self._board[3][box] = '▧' #wings
        self._board[2][6] = '▧' #middle
        for box in range(5, 8):
            self._board[1][box] = '▧' #tail
        #second plane
        self._board[6][5] = 'ᐅ' #cabin
        for box in range(4, 9):
            self._board[box][4] = '▣' #wings
        self._board[6][3] = '▣' #middle
        for box in range(5, 8):
            self._board[box][2] = '▣' #tail

    def create_scenario_5(self):
        #first plane
        self._board[3][2] = 'ᐊ' #cabin
        for box in range(1, 6):
            self._board[box][3] = '◼' #wings
        self._board[3][4] = '◼' #middle
        for box in range(2, 5):
            self._board[box][5] = '◼' #tail
        #second plane
        self._board[6][8] = 'ᐅ'  #cabin
        for box in range(4, 9):
            self._board[box][7] = '▣'  #wings
        self._board[6][6] = '▣'  #middle
        for box in range(5, 8):
            self._board[box][5] = '▣'  #tail

    def set_value_on_board(self, raw, column, element):
        self.set_value_on_mirror_board(raw, column, element)
        self._board[raw][column] = element

    def get_board(self):
        return self._board

    def get_mirror_board(self):
        return self._mirror_board

    def set_value_on_mirror_board(self, raw, column, element):
        self._mirror_board[raw][column] = element

class PlayerBoard(object):

    def __init__(self, validator):
        self._validate = validator
        self._board = []
        character_line = ['/', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for line in range(0, 9):
            self._board.append(["~"] * 9)
        for column in range(0, 9):
            self._board[0][column] = character_line[column]
        for line in range(1, 9):
            self._board[line][0] = str(line)

    def set_value_on_board(self, raw, column, element):
        self._board[raw][column] = element

    def get_board(self):
        return self._board

    def check_value_of_position(self, raw, column):
        if self._board[raw][column] == '~':
            return True
        else:
            return False

    def set_down_plane(self, raw, column):
        #set cabin of plane
        self._validate.validate_plane_of_player(self._board, raw, column)
        self._board[raw][column] = 'ᐁ'
        #set right and left wing
        left_wing = column - 2
        right_wing = column + 3
        for index in range(left_wing, right_wing):
            self._validate.validate_plane_of_player(self._board, raw - 1, index)
            self._board[raw - 1][index] = "▧"
        #set middle of plane
        self._validate.validate_plane_of_player(self._board, raw - 2, column)
        self._board[raw - 2][column] = '▧'
        #set left and right tail
        left_tail = column - 1
        right_tail = column + 2
        for index in range(left_tail, right_tail):
            self._validate.validate_plane_of_player(self._board, raw - 3, index)
            self._board[raw - 3][index] = '▧'

    def set_left_plane(self, raw, column):
        #set cabin
        self._validate.validate_plane_of_player(self._board, raw, column)
        self._board[raw][column] = 'ᐊ'
        #set wings
        right_wing = raw - 2
        left_wing = raw + 3
        for box in range(right_wing, left_wing):
            self._validate.validate_plane_of_player(self._board, box, column + 1)
            self._board[box][column + 1] = '◼'
        #set middle
        self._validate.validate_plane_of_player(self._board, raw, column + 2)
        self._board[raw][column + 2] = '◼'
        #set tail
        left_tail = raw - 1
        right_tail = raw + 2
        for box in range(left_tail, right_tail):
            self._validate.validate_plane_of_player(self._board, box, column + 3)
            self._board[box][column + 3] = '◼'

    def set_up_plane(self, raw, column):
        #set cabin
        self._validate.validate_plane_of_player(self._board, raw, column)
        self._board[raw][column] = 'ᐃ'
        #set wings
        left_wing = column - 2
        right_wing = column + 3
        for box in range(left_wing, right_wing):
            self._validate.validate_plane_of_player(self._board, raw + 1, box)
            self._board[raw + 1][box] = '◍'
        #set middle
        self._validate.validate_plane_of_player(self._board, raw + 2, column)
        self._board[raw + 2][column] = '◍'
        #set tail
        left_tail = column - 1
        right_tail = column + 2
        for box in range(left_tail, right_tail):
            self._validate.validate_plane_of_player(self._board, raw + 3, box)
            self._board[raw + 3][box] = '◍'

    def set_right_plane(self, raw, column):
        #set cabin
        self._validate.validate_plane_of_player(self._board, raw, column)
        self._board[raw][column] = 'ᐅ'
        #set wings
        left_wing = raw - 2
        right_wing = raw + 3
        for box in range(left_wing, right_wing):
            self._validate.validate_plane_of_player(self._board, box, column - 1)
            self._board[box][column - 1] = '▣'
        #set middle
        self._validate.validate_plane_of_player(self._board, raw, column - 2)
        self._board[raw][column - 2] = '▣'
        #set tail
        left_tail = raw - 1
        right_tail = raw + 2
        for box in range(left_tail, right_tail):
            self._validate.validate_plane_of_player(self._board, box, column - 3)
            self._board[box][column - 3] = '▣'



