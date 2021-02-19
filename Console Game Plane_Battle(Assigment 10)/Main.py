from Repository.board_repo import BoardToAttack, PlayerBoard
from Service.attack_service import Attack
from Tests.test_attack import TestAttack
from Tests.test_boardToAttack import TestBoardToAttack
from Tests.test_playerBoard import TestPlayerBoard
from UI.Console import UI
from Validations.validate import ValidateInputs

board_of_cmp = BoardToAttack()
board_of_player = PlayerBoard(ValidateInputs)
attack = Attack(board_of_cmp, board_of_player)
test_attack = TestAttack()
test_BoardToAttack = TestBoardToAttack()
test_PlayerBoard = TestPlayerBoard()
ui = UI(attack)

ui.run()
