import unittest
from unittest import TestCase

from Repository.board_repo import BoardToAttack, PlayerBoard
from Service.attack_service import Attack
from Validations.validate import ValidateInputs


class TestAttack(TestCase):

    def test_check_plane_down_for_cmp__correct_coordinates__expected_affirmative_response_of_found_target(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        cmp = BoardToAttack()
        cmp.set_value_on_board(8, 5, 'ᐊ')
        attack = Attack(cmp, player)
        self.assertEqual(attack.check_plane_down_for_cmp(8, 5), True)

    def test_check_plane_down_for_player__correct_coordinates__expected_affirmative_response_of_found_target(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        player.set_value_on_board(8, 5, 'ᐊ')
        self.assertEqual(attack.check_plane_down_for_player(8, 5), True)

    def test_mark_attack_on_player__correct_inputs__expected_correct_mark_at_coordinates_given(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_value_on_board(8, 5, '~')
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        attack.mark_attack_on_player(8, 5)
        self.assertEqual(player.check_value_of_target(8, 5, 'o'), True)

    def test_fill_stack_with_possible_targets__correct_inputs__expected_valid_append_in_list(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        attack.fill_stack_with_possible_targets(5, 6)
        self.assertNotEqual(attack._stack_of_targets, [])

    def test_hunt_mode__correct_inputs__expected_valid_addition_of_coordinates_in_list(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        coordinates = []
        attack.hunt_mode(coordinates)
        self.assertNotEqual(coordinates, [])

    def test_check_if_target__correct_inputs__expected_affirmative_response(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_value_on_board(8, 5, 'ᐊ')
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        self.assertTrue(attack.check_if_target(8, 5))

    def test_target_mode__correct_inputs__expected_valid_addition_of_coordinates_in_list(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        attack.fill_stack_with_possible_targets(5, 6)
        coordinates = []
        attack.target_mode(coordinates)
        self.assertNotEqual(coordinates[0], [])

    def test_attack_cmp__correct_inputs__expected_correct_mark_at_coordinates_given(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_value_on_board(8, 5, '~')
        cmp = BoardToAttack()
        attack = Attack(cmp, player)
        attack.attack_cmp(8, 5)
        self.assertEqual(cmp._board[8][5], 'o')

if __name__ == '__main__':
    unittest.main() # pragma: no cover