import unittest
from unittest import TestCase

from Repository.board_repo import PlayerBoard
from Validations.validate import ValidateInputs


class TestPlayerBoard(TestCase):

    def test_set_value_on_board__correct_input__expected_correct_mark_at_coordinates(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_value_on_board(2, 4, '#')
        self.assertEqual(player._board[2][4], '#')

    def test_check_value_of_target__correct_inputs__expected_correct_implementation_of_plane(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_value_on_board(2, 4, '#')
        self.assertEqual(player.check_value_of_target(2, 4, '#'), True)

    def test_set_down_plane__correct_inputs__expected_correct_implementation_of_plane(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_down_plane(8, 5)
        self.assertEqual(player._board[8][5], 'ᐁ')

    def test_set_left_plane__correct_inputs__expected_correct_implementation_of_plane(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_left_plane(6, 1)
        self.assertEqual(player._board[6][1], 'ᐊ')

    def test_set_up_plane__correct_inputs__expected_correct_implementation_of_plane(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_up_plane(1, 4)
        self.assertEqual(player._board[1][4], 'ᐃ')

    def test_set_right_plane(self):
        validation = ValidateInputs()
        player = PlayerBoard(validation)
        player.set_right_plane(5, 8)
        self.assertEqual(player._board[5][8], 'ᐅ')

if __name__ == '__main__':
    unittest.main() # pragma: no cover