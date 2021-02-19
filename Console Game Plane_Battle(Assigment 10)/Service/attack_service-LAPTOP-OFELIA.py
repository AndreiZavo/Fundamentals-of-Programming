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
        #test if a plane of cmp's is down
        board = self._board_of_cmp.get_board()
        if board[raw][column] in ['ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            return True
        else:
            return False

    def check_plane_down_for_player(self, raw, column):
        #test if a plane of player's if down
        board = self._board_of_player.get_board()
        if board[raw][column] in ['ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            return True
        else:
            return False

    def mark_attack_player(self, random_raw, random_column):
        #the cmp attacks the player
        hit = self.check_plane_down_for_player(random_raw, random_column)
        board = self._board_of_player.get_board()
        if board[random_raw][random_column] in ['▣', '◍', '◼', '▧', '~']:
            self._board_of_player.set_value_on_board(random_raw, random_column, 'x')
        elif hit:
            self._board_of_player.set_value_on_board(random_raw, random_column, '💔')
        else:
            self._board_of_player.set_value_on_board(random_raw, random_column, 'o')

    def attack_player_hunt_mode(self):
        while True:
            random_raw = random.randint(1, 8)
            random_column = random.randint(1, 8)
            coordinates = [random_raw, random_column]
            return coordinates

    @staticmethod
    def attack_player_fill_the_stack_with_possible_targets(raw, column, stack_of_possible_targets):
        north_target = [raw - 1, column]
        south_target = [raw + 1, column]
        east_target = [raw, column + 1]
        west_target = [raw, column - 1]
        stack_of_possible_targets.append(north_target)
        stack_of_possible_targets.append(south_target)
        stack_of_possible_targets.append(east_target)
        stack_of_possible_targets.append(west_target)

    def attack_player_target_mode(self, raw, column):
        self.attack_player_fill_the_stack_with_possible_targets(raw, column, self._stack_of_targets)
        print(self._stack_of_targets)
        if not self._stack_of_targets:
            while True:
                random_raw = random.randint(1, 8)
                random_column = random.randint(1, 8)
                if self._board_of_player.check_value_of_position(random_raw, random_column):
                    coordinates = [random_raw, random_column]
                    return coordinates
        else:
            coordinates = self._stack_of_targets[-1]
            self._stack_of_targets.pop()
            return coordinates

    def attack_cmp(self, raw, column):
        #the player attacks
        board = self._board_of_cmp.get_board()
        hit = self.check_plane_down_for_cmp(raw, column)
        if board[raw][column] not in ['~', 'ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']:
            self._board_of_cmp.set_value_on_board(raw, column, 'x')
        elif hit:
            self._board_of_cmp.set_value_on_board(raw, column, '💔')
        else:
            self._board_of_cmp.set_value_on_board(raw, column, 'o')

    def show_symbol_to_be_targeted(self, raw, column, elements):
        board = self._board_of_player.get_board()
        if board[raw][column] in elements:
            return True
        else:
            return False
