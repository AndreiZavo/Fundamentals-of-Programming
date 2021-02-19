import random

from Validations.validate import ValidateInputs


class UI(object):

    def __init__(self, service):
        self._service = service

    @staticmethod
    def begin():
        print("Let's play Planes!")
        print("You will start with introducing two coordinates. One for row, one for column. Then the PC will do the same!")
        print('Good luck!')

    def put_planes_on_board(self):
        print("Please insert two sets of coordinates for your planes: ")
        print("Select the orientation for the first plane. These are your options: ")
        print(" ᐊ - West      ᐁ - South       ᐃ - North       ᐅ - East ")
        choice = {
            '1': self._service.set_left_plane,
            '2': self._service.set_down_plane,
            '3': self._service.set_up_plane,
            '4': self._service.set_right_plane
        }
        print()
        self.show_player_board()
        index = 0
        while index < 2:
            if index == 0:
                print("First plane: ")
            command = input("Insert the direction correspondingly from 1 to 4: ")
            raw = int(input("Raw: "))
            column = input("Column: ")
            column = self.convert_latter_to_number(column)
            ValidateInputs.validate_coordinates_of_player(raw, column)
            if command in choice:
                choice[command](raw, column)
            else:
                raise TypeError("Insert a valid value")
            self.show_player_board()
            if index == 0:
                print("Second plane: ")
            index += 1

    def convert_latter_to_number(self, letter):
        letter = ord(letter) - 96
        return letter

    def coordinates_for_attack(self):
        number_of_down_planes_by_player = 0
        number_of_down_planes_by_cmp = 0
        while True:
            raw = int(input("Insert the raw of your attack: "))
            column = input("Insert the column of your attack: ")
            column = int(self.convert_latter_to_number(column))
            hit_cmp = self._service.check_plane_down_for_cmp(raw, column)
            ValidateInputs.validate_coordinates_of_player(raw, column)
            self._service.attack_cmp(raw, column)
            if hit_cmp:
                if number_of_down_planes_by_player == 0:
                    print("Nice! You took down a plane!")
                    number_of_down_planes_by_player += 1
                else:
                    print("Incredible! You WON!!")
                    return
            coordinates = []
            self._service.target_mode(coordinates)
            raw_to_shoot = coordinates[0][0]
            column_to_shoot = coordinates[0][1]
            if self._service.check_if_target(raw_to_shoot, column_to_shoot):
                self._service.fill_stack_with_possible_targets(raw_to_shoot, column_to_shoot)
            hit_player = self._service.check_plane_down_for_player(raw_to_shoot, column_to_shoot)
            self._service.mark_attack_on_player(raw_to_shoot, column_to_shoot)
            if hit_player:
                if number_of_down_planes_by_cmp == 0:
                    print("Oh no! The adversary took down a plane!")
                    number_of_down_planes_by_cmp += 1
                else:
                    print("Unfortunately! You lost..")
                    return
            self.show_enemy_mirror_board()
            print('\n')
            self.show_player_board()

    def show_enemy_board(self):
        for line in self._service.show_board_cmp():
            print(" ".join(line))

    def show_enemy_mirror_board(self):
        for line in self._service.show_mirror_board_cmp():
            print(" ".join(line))

    def show_player_board(self):
        for line in self._service.show_board_player():
            print(" ".join(line))

    def run(self):
        self.begin()
        self.put_planes_on_board()
        self.coordinates_for_attack()