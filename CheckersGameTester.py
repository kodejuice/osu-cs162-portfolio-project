import unittest
from CheckersGame import *


class TestCheckersGame(unittest.TestCase):
  def setUp(self):
    self.game = Checkers()
    self.player1 = self.game.create_player("Adam", "White")
    self.player2 = self.game.create_player("Lucy", "Black")

  def test_create_player(self):
    self.assertEqual(self.player1.player_name, "Adam")
    self.assertEqual(self.player1.checker_color, "White")
    self.assertEqual(self.player2.player_name, "Lucy")
    self.assertEqual(self.player2.checker_color, "Black")

  def test_play_game(self):
    # Test for valid move
    self.assertEqual(self.game.play_game("Lucy", (5, 6), (4, 7)), 0)
    self.assertEqual(self.game.play_game("Adam", (2, 1), (3, 0)), 0)

    # Test for invalid player_name
    with self.assertRaises(InvalidPlayer):
      self.game.play_game("John", (2, 1), (3, 0))

    # Test for invalid square_location
    with self.assertRaises(InvalidSquare):
      self.game.play_game("Adam", (9, 9), (3, 0))

    # Test for out of turn
    with self.assertRaises(OutofTurn):
      self.game.play_game("Adam", (2, 1), (3, 0))

  def test_get_checker_details(self):
    # Test for valid square_location
    self.assertEqual(self.game.get_checker_details((3, 1)), None)
    self.assertEqual(self.game.get_checker_details((0, 1)), 'White')

    # Test for invalid square_location
    with self.assertRaises(InvalidSquare):
      self.game.get_checker_details((9, 9))

  def test_max_capture_rule(self):
    # Test max capture rule
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', 'W', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', 'W', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'W', '-', 'W', '-', '-'],
        ['-', '-', '-', '-', 'B', '-', '-', '-'],
    ])
    self.game.board = test_board

    # Single capture move should be an invalid move
    with self.assertRaises(InvalidSquare):
      self.game.play_game("Lucy", (7, 4), (5, 2))

    # 3 captures for second move
    self.assertEqual(self.game.play_game('Lucy', (7, 4), (5, 6)), 3)

    # test the new board position
    self.assertEqual(self.game.board, B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', 'B', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'W', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

  def test_king_promotion(self):
    # Test King promotion
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'B', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'W', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'W', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # promote black
    self.game.play_game('Lucy', (1, 2), (0, 1))

    # check king count
    self.assertEqual(self.player2.get_king_count(), 1)

    # check new baord position
    self.assertEqual(self.game.board, B([
        ['-', 'Bk', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'W', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'W', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

    # test compulsory capture and promote

    # Non capture move from white should be an invalid move
    with self.assertRaises(InvalidSquare):
      self.game.play_game("Adam", (5, 2), (6, 1))

    # promote white piece
    self.game.play_game("Adam", (5, 2), (7, 4))

    # check king count
    self.assertEqual(self.player1.get_king_count(), 1)

    # check new baord position
    self.assertEqual(self.game.board, B([
        ['-', 'Bk', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'W', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'Wk', '-', '-', '-'],
    ]))

  def test_triple_king_promotion(self):
    # Test Triple King Promotion
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'Wk', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'Bk', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # promote black to triple king
    self.game.play_game('Lucy', (6, 2), (7, 1))
    self.assertEqual(self.player2.get_triple_king_count(), 1)

    # promote white to triple king
    self.game.play_game('Adam', (1, 2), (0, 1))
    self.assertEqual(self.player1.get_triple_king_count(), 1)

  def test_friendly_jump(self):
    # Test Friendly jump
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'B*', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # jump friendly piece
    self.game.play_game('Lucy', (1, 2), (3, 4))

    # check new position
    self.assertEqual(self.game.board, B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'B*', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

  def test_double_piece_jump(self):
    # Test enemy double piece jump
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'B*', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'W', '-', '-', '-', 'W*'],
        ['-', '-', '-', '-', 'W', '-', 'B', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # jump double checkers and check captured pieces count (=2)
    self.assertEqual(self.game.play_game('Lucy', (1, 2), (4, 5)), 2)

    # check new position
    self.assertEqual(self.game.board, B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', 'W*'],
        ['-', '-', '-', '-', '-', '-', 'B', '-'],
        ['-', '-', '-', '-', '-', 'B*', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

    # jump double checkers and check captured pieces count (=2)
    self.assertEqual(self.game.play_game('Adam', (2, 7), (5, 4)), 2)

    # check new position
    self.assertEqual(self.game.board, B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'W*', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

  def test_game_winner(self):
    # Test game winner method
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['W', '-', '-', '-', 'W', '-', '-', '-'],
        ['-', 'W', '-', 'W', '-', '-', '-', '-'],
        ['-', '-', 'B', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # black to move, but has no moves
    self.assertEqual(self.game.game_winner(), 'Adam')  # white wins

    # test black win
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['W', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'W', '-', '-', '-', '-', '-', '-'],
        ['B', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'B', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board

    # move black piece
    self.game.play_game('Lucy', (6, 1), (5, 2))

    # now white has to move and has no move
    self.assertEqual(self.game.game_winner(), 'Lucy')  # black wins
    self.assertEqual(self.game.board, B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['W', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'W', '-', '-', '-', '-', '-', '-'],
        ['B', '-', 'B', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]))

    # test for no piece win
    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board
    self.assertEqual(self.game.game_winner(), 'Lucy')  # black wins

    test_board = B([
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'W', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ])
    self.game.board = test_board
    self.assertEqual(self.game.game_winner(), 'Adam')  # white wins


def B(board):
  """We'll use this to convert a simpler representation of the checkers board"""
  b = [[None for _ in range(8)] for _ in range(8)]
  for r in range(8):
    for c in range(8):
      p = board[r][c].lower()
      if p == '-':
        b[r][c] = None
      if p == 'b':
        b[r][c] = 'Black'
      if p == 'bk':
        b[r][c] = 'Black_king'
      if p == 'b*':
        b[r][c] = 'Black_Triple_King'
      if p == 'w':
        b[r][c] = 'White'
      if p == 'wk':
        b[r][c] = 'White_king'
      if p == 'w*':
        b[r][c] = 'White_Triple_King'
  return b


if __name__ == '__main__':
  unittest.main()
