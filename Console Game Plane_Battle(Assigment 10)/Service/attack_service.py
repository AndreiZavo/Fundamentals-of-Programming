import random


class Attack(object):

    def __init__(self, board_of_cmp, board_of_player):
        self._board_of_cmp = board_of_cmp
        self._board_of_player = board_of_player
        self._stack_of_targets = []

    def set_down_plane(self, raw, column):
        self._board_of_player.set_down_plane(raw, column)

    def set_left_plane(self, raw, column):
        self._board_of_player.set_left_plane(raw, column)

    def set_up_plane(self, raw, column):
        self._board_of_player.set_up_plane(raw, column)

    def set_right_plane(self, raw, column):
        self._board_of_player.set_right_plane(raw, column)

    def show_board_player(self):
        return self._board_of_player.get_board()

    def show_board_cmp(self):
        return self._board_of_cmp.get_board()

    def show_mirror_board_cmp(self):
        return self._board_of_cmp.get_mirror_board()

    def check_plane_down_for_cmp(self, raw, column):
        # test if a plane of cmp's is down
        board = self._board_of_cmp.get_board()
        if board[raw][column] in ['ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            return True
        else:
            return False

    def check_plane_down_for_player(self, raw, column):
        # test if a plane of player's if down
        board = self._board_of_player.get_board()
        if board[raw][column] in ['ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            return True
        else:
            return False

    def mark_attack_on_player(self, random_raw, random_column):
        # the cmp attacks the player
        hit = self.check_plane_down_for_player(random_raw, random_column)
        board = self._board_of_player.get_board()
        if board[random_raw][random_column] not in ['~', 'ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            self._board_of_player.set_value_on_board(random_raw, random_column, 'x')
        elif hit:
            self._board_of_player.set_value_on_board(random_raw, random_column, '💔')
        else:
            self._board_of_player.set_value_on_board(random_raw, random_column, 'o')

    def fill_stack_with_possible_targets(self, raw, column):
        # fill the stack with the neighbours of a good hit
        board = self._board_of_player.get_board()
        north_target = [raw - 1, column]
        east_target = [raw, column + 1]
        south_target = [raw + 1, column]
        west_target = [raw, column - 1]
        if board[raw - 1][column] not in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6',
                                          '7', '8']:
            self._stack_of_targets.append(north_target)
        if board[raw][column + 1] not in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6',
                                          '7', '8']:
            self._stack_of_targets.append(east_target)
        if board[raw][column - 1] not in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6',
                                          '7', '8']:
            self._stack_of_targets.append(west_target)
        if board[raw + 1][column] not in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6',
                                          '7', '8']:
            self._stack_of_targets.append(south_target)

    def hunt_mode(self, coordinates_to_shoot):
        # used for searching randomly for a target
        while True:
            random_raw = random.randint(1, 8)
            random_column = random.randint(1, 8)
            if not self._board_of_player.check_value_of_target(random_raw, random_column, ['x', '💔', 'o']):
                coordinates = [random_raw, random_column]
                coordinates_to_shoot.append(coordinates)
                return

    def check_if_target(self, raw, column):
        # check if an element on coordinates given is a good hit
        if not self._board_of_player.check_value_of_target(raw, column, ['x', '💔', 'o', '~']):
            return True
        else:
            return False

    def target_mode(self, coordinates_to_shoot):
        # used when the cmp found a valid target
        if self._stack_of_targets != []:
            coordinates = self._stack_of_targets[-1]
            self._stack_of_targets.pop()
            coordinates_to_shoot.append(coordinates)
            return
        else:
            self.hunt_mode(coordinates_to_shoot)

    def attack_cmp(self, raw, column):
        # the player attacks
        board = self._board_of_cmp.get_board()
        hit = self.check_plane_down_for_cmp(raw, column)
        if board[raw][column] not in ['~', 'ᐊ', 'ᐁ', 'ᐃ', 'ᐅ', 'o']:
            self._board_of_cmp.set_value_on_board(raw, column, 'x')
        elif hit:
            self._board_of_cmp.set_value_on_board(raw, column, '💔')
        else:
            self._board_of_cmp.set_value_on_board(raw, column, 'o')
