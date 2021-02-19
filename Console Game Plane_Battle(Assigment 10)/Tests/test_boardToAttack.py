import unittest
from unittest import TestCase

from Repository.board_repo import BoardToAttack


class TestBoardToAttack(TestCase):

    def test_create_board__correct_inputs__expected_correct_creation_of_the_board(self):
        board_to_attack = BoardToAttack()
        assert board_to_attack._board != []

    def test_set_value_on_board__correct_coordinates__expected_correct_mark_on_board(self):
        board_to_attack = BoardToAttack()
        board_to_attack.set_value_on_board(2, 4, '$')
        self.assertEqual(board_to_attack._board[2][4], '$')

if __name__ == '__main__':
    unittest.main() # pragma: no cover