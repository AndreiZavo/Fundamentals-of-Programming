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
        index = 0
        while index < 2:
            if index == 0:
                print("First plane: ")
            command = input("Insert the direction correspondingly from 1 to 4: ")
            raw = int(input("Raw: "))
            column = input("Column ")
            column = int(self.convert_latter_to_number(column))
            ValidateInputs.validate_coordinates_of_player(raw, column)
            if command in choice:
                choice[command](raw, column)
            else:
                raise TypeError("Insert a valid value")
            self.show_player_board()
            if index == 0:
                print("Second plane: ")
            index += 1

    @staticmethod
    def convert_latter_to_number(letter):
        letter = ord(letter) - 96
        return letter

    def coordinates_for_attack(self):
        number_of_down_planes_by_player = 0
        number_of_down_planes_by_cmp = 0
        target_found = False
        coordinates = []
        coordinates_of_found_target = []
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
            #the cmp attacks
            if not target_found:        #test the case of the first ever attack
                coordinates = self._service.attack_player_hunt_mode()
            if target_found:
                print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                coordinates = self._service.attack_player_target_mode(coordinates_of_found_target[0], coordinates_of_found_target[1])
                print(coordinates)
                if self._service.show_symbol_to_be_targeted(coordinates[0], coordinates[1], ['ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']):
                    target_found = False
            raw_to_attack = coordinates[0]
            column_to_attack = coordinates[1]
            hit_player = self._service.check_plane_down_for_player(raw_to_attack, column_to_attack)
            self._service.mark_attack_player(raw_to_attack, column_to_attack)
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
            if not target_found:
                if self._service.show_symbol_to_be_targeted(coordinates[0], coordinates[1], ['▣', '◍', '◼', '▧', 'ᐊ', 'ᐁ', 'ᐃ', 'ᐅ']):
                    target_found = True
                    coordinates_of_found_target = coordinates

    def show_enemy_board(self):
        for line in self._service.show_board_cmp():
            print(" ".join(line))

    def show_enemy_mirror_board(self):
        for line in self._service.show_mirror_board_cmp():
            print(" ".join(line))

    def show_player_board(self):
        for line in self._service.show_board_player():
            print(" ".join(line))
    

