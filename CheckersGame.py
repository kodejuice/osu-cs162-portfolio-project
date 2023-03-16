# Author: Biereagu Sochima
# GitHub username: kodejuice
# Date: X/02/2023
# Description: Checkers game


"""
For this project you will write a class called Checkers that allows two people to play the game of Checkers. This is a variation of the original Checkers game with modified rules. Read about the Game rules in Checkers.pdf

Checkers:

The Checkers object represents the game as played.

The class should contain information about the board and the players. The board is initialized when the Checkers object is created.

It must contain these methods (but may have more if you want):

create_player - takes as parameter the player_name and piece_color that the player wants to play with and creates the player object. The parameter piece_color is a string of value "Black" or "White" representing Black or White checkers pieces respectively. This function returns the player object that has been created.

play_game - takes as parameter player_name, starting_square_location and destination_square_location of the piece that the player wants to move. The square_location is a tuple in format (x,y).
If a player wants to move a piece from third square in the second row to fourth square in the fifth row, the starting and destination square locations will be (1,2) to (4,3). Following the rules of the game move this piece.

If a player attempts to move a piece out of turn, raise an OutofTurn exception (you'll need to define this exception class).
If a player does not own the checker present in the square_location or if the square_location does not exist on the baord; raise an InvalidSquare exception (you'll need to define this exception class).
If the player_name is not valid, raise an InvalidPlayer exception (you'll need to define this exception class).
This method returns the number of captured pieces, if any, otherwise return 0.
If the destination piece reaches the end of opponent's side it is promoted as a king on the board. If the piece crosses back to its original side it becomes a triple king.
If the piece being moved is a king or a triple king assess the move according to the rules of the game.

get_checker_details - takes as parameter a square_location on the board and returns the checker details present in the square_location

Returns None, if no piece is present in the location
If the square_location does not exist on the board, raise an InvalidSquare exception (use the same exception class that was created for play_game function).
If black piece is present return "Black"
If white piece is present return "White"
If black king piece is present return "Black_king"
If white king piece is present return "White_king"
If black triple king piece is present return "Black_Triple_King"
If white triple king piece is present return "White_Triple_King"

print_board - takes no parameter, prints the current board in the form of an array. Below is an example showing the current board in the initial state (Note, here only the first row is printed, you would print the entire board)

[[None, "White", None, "White", None, "White", None, "White"],....]

*game_winner - takes no parameter, returns the name of player who won the game. If the game has not ended, return "Game has not ended". In this function you need not check this condition - "A less common way to win is when all of your opponent's pieces are blocked so that your opponent can't make any more moves."

Player:

Player object represents the player in the game. It is initialized with player_name and checker_color that the player has chosen. The parameter piece_color is a string of value "Black" or "White".

get_king_count - takes no parameter, returns the number of king pieces that the player has
get_triple_king_count - takes no parameter, returns the number of triple king pieces that the player has
get_captured_pieces_count - takes no parameter, returns the number of opponent pieces that the player has captured
In addition to your file containing the code for the above classes, **you must also submit a file that contains unit tests for your classes. It must have at least five unit tests and use at least two different assert functions.

Your files must be named CheckersGame.py and CheckersGameTester.py

For example, your classes will be used as below:

game = Checkers()
Player1 = game.create_player("Adam", "White")

Player2 = game.create_player("Lucy", "Black")

game.play_game("Lucy", (5, 6), (4, 7))

game.play_game("Adam", (2,1), (3,0))

game.get_checker_details((3,1))

Player1.get_captured_pieces_count()
"""


# CheckersGame.py

# Error classes
class OutofTurn(Exception):
  """Raised when a player attempts to move a piece out of turn"""
  pass


class InvalidSquare(Exception):
  """Raised when a player attempts to move a piece to an invalid square"""
  pass


class InvalidPlayer(Exception):
  """Raised when the player name is not valid"""
  pass


class Player:
  """Represents the player in the game. It is initialized with player_name and checker_color that the player has chosen."""

  def __init__(self, player_name, checker_color):
    self.player_name = player_name
    self.checker_color = checker_color
    self.king_count = 0
    self.triple_king_count = 0
    self.captured_pieces_count = 0

  def get_king_count(self):
    """Returns the number of king pieces that the player has."""
    return self.king_count

  def get_triple_king_count(self):
    """Returns the number of triple king pieces that the player has."""
    return self.triple_king_count

  def get_captured_pieces_count(self):
    """Returns the number of opponent pieces that the player has captured."""
    return self.captured_pieces_count

  def increment_king_count(self):
    """Increases the number of king pieces that the player has."""
    self.king_count += 1

  def increment_triple_king_count(self):
    """Increases the number of triple king pieces that the player has."""
    self.triple_king_count += 1

  def increment_captured_pieces_count(self):
    """Increases the number of opponent pieces that the player has captured."""
    self.captured_pieces_count += 1


class Checkers:
  """The Checkers object represents the game as played.
  The class should contain information about the board and the players."""

  def __init__(self, player1=None, player2=None):
    # Initializing the board
    self.board = [[None for _ in range(8)] for _ in range(8)]
    # Setting up the pieces for player 1
    for row in range(3):
      for col in range(8):
        if row % 2 == 0:
          if col % 2 == 1:
            self.board[row][col] = "White"
        else:
          if col % 2 == 0:
            self.board[row][col] = "White"
    # Setting up the pieces for player 2
    for row in range(5, 8):
      for col in range(8):
        if row % 2 == 0:
          if col % 2 == 1:
            self.board[row][col] = "Black"
        else:
          if col % 2 == 0:
            self.board[row][col] = "Black"
    self.player1 = player1
    self.player2 = player2

  def create_player(self, player_name, piece_color):
    """Creates a player object with the given player_name and piece_color.
    The parameter piece_color is a string of value "Black" or "White" representing Black or White checkers pieces respectively.
    This function returns the player object that has been created."""
    return Player(player_name, piece_color)

  def get_checker_details(self, square_location):
    """Takes as parameter a square_location on the board and returns the checker details present in the square_location.
      Returns None if no piece is present in the location.
      If the square_location does not exist on the board, raise an InvalidSquare exception.
      If black piece is present return "Black".
      If white piece is present return "White".
      If black king piece is present return "Black_king".
      If white king piece is present return "White_king".
      If black triple king piece is present return "Black_Triple_King".
      If white triple king piece is present return "White_Triple_King"."""
    row, col = square_location
    if not self._in_bound((row, col)):
      raise InvalidSquare("Invalid square entered.")
    return self.board[row][col]

  def _get_moves(self, square_location):
    """Return all possible moves from a given square location"""
    piece = self.get_checker_details(square_location)
    if not piece:
      return []
    top_left_squares = self._diagonal_squares(square_location, -1, -1)
    top_right_squares = self._diagonal_squares(square_location, -1, 1)
    bottom_left_squares = self._diagonal_squares(square_location, 1, -1)
    bottom_right_squares = self._diagonal_squares(square_location, 1, 1)

    if self._is_triple_king(piece):
      # Triple King
      color = 'White' if self._is_black_piece(piece) else 'Black'  # opponent
      top_left = self._get_valid_moves(top_left_squares, color, False, True)
      top_right = self._get_valid_moves(top_right_squares, color, False, True)
      bottom_left = self._get_valid_moves(
          bottom_left_squares, color, False, True)
      bottom_right = self._get_valid_moves(
          bottom_right_squares, color, False, True)
      moves = top_left + top_right + bottom_left + bottom_right

    elif self._is_king(piece):
      # King
      color = 'White' if self._is_black_piece(piece) else 'Black'  # opponent
      top_left = self._get_valid_moves(top_left_squares, color, False)
      top_right = self._get_valid_moves(top_right_squares, color, False)
      bottom_left = self._get_valid_moves(bottom_left_squares, color, False)
      bottom_right = self._get_valid_moves(bottom_right_squares, color, False)
      moves = top_left + top_right + bottom_left + bottom_right

    elif self._is_black_piece(piece):
      # Black Piece
      top_left_moves = self._get_valid_moves(top_left_squares, 'White')
      top_right_moves = self._get_valid_moves(top_right_squares, 'White')
      moves = top_left_moves + top_right_moves

    else:
      # White Piece
      bottom_left_moves = self._get_valid_moves(bottom_left_squares, 'Black')
      bottom_right_moves = self._get_valid_moves(bottom_right_squares, 'Black')
      moves = bottom_left_moves + bottom_right_moves

    captures = [m for m in moves if m[1] == True]
    return captures or moves

  def _get_valid_moves(self, diagonal_squares, piece, is_man=True, is_triple=False):
    """Get list of all valid moves in a diagonal for opponent of given piece type"""
    all_moves, all_captures = [], []
    friendly = False
    N = len(diagonal_squares)

    for i in range(N):
      checker = self.get_checker_details(diagonal_squares[i])

      if is_man:
        if checker == None:
          return [(diagonal_squares[i], False)]
        if piece in checker:
          if i < N-1 and self.get_checker_details(diagonal_squares[i+1]) == None:
            return [(diagonal_squares[i+1], True)]
        return []

      if checker != None:
        if i == N-1:
          break

        next_checker = self.get_checker_details(diagonal_squares[i+1])
        if piece not in checker:
          # mark for Triple friendly
          if not friendly and next_checker == None and is_triple:
            friendly = True
            continue
          break

        jump = 1
        if (next_checker != None and not is_triple):
          break
        elif next_checker:
          # Triple king double enemy jump
          if piece in next_checker and i < N-2 and self.get_checker_details(diagonal_squares[i+2]) == None:
            jump = 2

        for j in range(i + jump, N):
          c = self.get_checker_details(diagonal_squares[j])
          if c != None:
            break
          all_captures += [(diagonal_squares[j], True)]
        break
      else:
        if not all_moves or friendly:
          all_moves += [(diagonal_squares[i], False)]
    return all_captures or all_moves

  def _diagonal_squares(self, square, dx, dy):
    """Return diagonal moves from a given square"""
    squares = []
    square = list(square)
    while True:
      square[0] += dx
      square[1] += dy
      if not self._in_bound(square):
        break
      squares += [tuple(square)]
    return squares

  def _diagonal_coord(self, start, stop):
    """Return coordinates in between two points along a diagonal path"""
    def coords(dxdy):
      r, c = start
      dx, dy = dxdy
      coords = []
      while (r, c) != stop:
        r += dx
        c += dy
        if not self._in_bound((r, c)):
          break
        coords += [(r, c)]
      return coords
    r1, c1 = start
    r2, c2 = stop
    P = (+(r1 != r2) if r2 >= r1 else -1, -(c1 != c2) if c2 <= c1 else +1)
    return coords(P)

  def _in_bound(self, square):
    """Check if given square position is in bound"""
    row, col = square
    return (row >= 0 and row <= 7 and col >= 0 and col <= 7)

  def _is_king(self, piece):
    """Check if a piece is king"""
    return 'ing' in piece.lower()

  def _is_triple_king(self, piece):
    """Check if a piece is Triple king"""
    return 'triple' in piece.lower()

  def _is_black_piece(self, piece):
    """Check if a piece is Black"""
    return 'black' in piece.lower()

    """
  # def play_game(self, player_name, start_location, destination_location):
  #   Makes a move with the given player_name, starting_square_location and destination_square_location of the piece.
  #   The square_location is a tuple in format (x,y).
  #   If a player attempts to move a piece out of turn, raise an OutofTurn exception.
  #   If a player does not own the checker present in the square_location or if the square_location does not exist on the baord; raise an InvalidSquare exception.
  #   If the player_name is not valid, raise an InvalidPlayer exception.
  #   This method returns the number of captured pieces, if any, otherwise return 0.
  #   If the destination piece reaches the end of opponent's side it is promoted as a king on the board. If the piece crosses back to its original side it becomes a triple king.
  #   If the piece being moved is a king or a triple king assess the move according to the rules of the game.
  #   # Checking if the player name is valid
  #   if player_name != self.player1.player_name and player_name != self.player2.player_name:
  #     raise InvalidPlayer
  #   # Checking if the start location is valid
  #   if start_location[0] < 0 or start_location[0] > 7 or start_location[1] < 0 or start_location[1] > 7:
  #     raise InvalidSquare
  #   # Checking if the destination location is valid
  #   if destination_location[0] < 0 or destination_location[0] > 7 or destination_location[1] < 0 or destination_location[1] > 7:
  #     raise InvalidSquare
  #   # Checking if the player is attempting to move a piece out of turn
  #   if player_name == self.player1.player_name:
  #     if self.board[start_location[0]][start_location[1]] != "White" and self.board[start_location[0]][start_location[1]] != "White_King" and self.board[start_location[0]][start_location[1]] != "White_Triple_King":
  #       raise OutofTurn
  #   elif player_name == self.player2.player_name:
  #     if self.board[start_location[0]][start_location[1]] != "Black" and self.board[start_location[0]][start_location[1]] != "Black_King" and self.board[start_location[0]][start_location[1]] != "Black_Triple_King":
  #       raise OutofTurn
  #   # Checking if the player owns the checker present in the start location
  #   if player_name == self.player1.player_name:
  #     if self.board[start_location[0]][start_location[1]] != "White" and self.board[start_location[0]][start_location[1]] != "White_King" and self.board[start_location[0]][start_location[1]] != "White_Triple_King":
  #       raise InvalidSquare
  #   elif player_name == self.player2.player_name:
  #     if self.board[start_location[0]][start_location[1]] != "Black" and self.board[start_location[0]][start_location[1]] != "Black_King" and self.board[start_location[0]][start_location[1]] != "Black_Triple_King":
  #       raise InvalidSquare
  #   # Making the move
  #   captured_pieces = 0
  #   # Checking if the move is a single move
  #   if abs(start_location[0] - destination_location[0]) == 1 and abs(start_location[1] - destination_location[1]) == 1:
  #     self.board[destination_location[0]][destination_location[1]
  #                                         ] = self.board[start_location[0]][start_location[1]]
  #     self.board[start_location[0]][start_location[1]] = None
  #     # Checking if the destination piece reaches the end of opponent's side
  #     if destination_location[0] == 0 and player_name == self.player1.player_name:
  #       self.board[destination_location[0]
  #                  ][destination_location[1]] = "White_King"
  #       self.player1.increment_king_count()
  #     elif destination_location[0] == 7 and player_name == self.player2.player_name:
  #       self.board[destination_location[0]
  #                  ][destination_location[1]] = "Black_King"
  #       self.player2.increment_king_count()
  #     # Checking if the piece crosses back to its original side
  #     if destination_location[0] == 3 and player_name == self.player1.player_name and self.board[destination_location[0]][destination_location[1]] == "White_King":
  #       self.board[destination_location[0]
  #                  ][destination_location[1]] = "White_Triple_King"
  #       self.player1.increment_triple_king_count()
  #     elif destination_location[0] == 4 and player_name == self.player2.player_name and self.board[destination_location[0]][destination_location[1]] == "Black_King":
  #       self.board[destination_location[0]
  #                  ][destination_location[1]] = "Black_Triple_King"
  #       self.player2.increment_triple_king_count()
  #   # Checking if the move is a jump move
  #   elif abs(start_location[0] - destination_location[0]) == 2 and abs(start_location[1] - destination_location[1]) == 2:
  #     # Checking if there is an opponent piece to jump over
  #     if player_name == self.player1.player_name:
  #       if self.board[(start_location[0]+destination_location[0])//2][(start_location[1]+destination_location[1])//2] != "Black" and self.board[(start_location[0]+destination_location[0])//2][(start_location[1]+destination_location[1])//2] != "Black_King" and self.board[(start_location[0]+destination_location[0])//2][(start_location[1]+destination_location[1])//2] != "Black_Triple_King":
  #         raise InvalidSquare
  #       else:
  #         captured_pieces = 1
  #         self.board[destination_location[0]][destination_location[1]
  #                                             ] = self.board[start_location[0]][start_location[1]]
  #         self.board[(start_location[0]+destination_location[0]) //
  #                    2][(start_location[1]+destination_location[1])//2] = None
  #         self.board[start_location[0]][start_location[1]] = None
  #         # Checking if the destination piece reaches the end of opponent's side
  #         if destination_location[0] == 0:
  #           self.board[destination_location[0]
  #                      ][destination_location[1]] = "White_King"
  #           self.player1.increment_king_count()
  #         # Checking if the piece crosses back to its original side
  #         if destination_location[0] == 3 and self.board[destination_location[0]][destination_location[1]] == "White_King":
  #           self.board[destination_location[0]
  #                      ][destination_location[1]] = "White_Triple_King"
  #           self.player1.increment_triple_king_count()
  #     elif player_name == self.player2.player_name:
  #       if self.board[(start_location[0]+destination_location[0])//2][(start_location[1]+destination_location[1])//2] != "White" and self.board[(start_location[0]+destination_location[0])//2][(start_location[1]+destination_location[1])//2] != "White
    """


game = Checkers()
Player1 = game.create_player("Adam", "White")
Player2 = game.create_player("Lucy", "Black")

# game.play_game("Lucy", (5, 6), (4, 7))
# game.play_game("Adam", (2, 1), (3, 0))
# game.get_checker_details((3, 1))
# Player1.get_captured_pieces_count()

# Checkers:
# - play_game
# - game_winner
# </>
# - create_player
# - print_board
# - get_checker_details


"""
[None, 'White', None, 'White', None, 'White', None, 'White']
['White', None, 'White', None, 'White', None, 'White', None]
[None, 'White', None, 'White', None, 'White', None, 'White']
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
['Black', None, 'Black', None, 'Black', None, 'Black', None]
[None, 'Black', None, 'Black', None, 'Black', None, 'Black']
['Black', None, 'Black', None, 'Black', None, 'Black', None]
"""

# game.board[3][4] = 'Black'
# game.board[4][1] = 'Black_king'
game.board[4][1] = 'Black_Triple_King'
game.board[3][2] = 'White'
game.board[4][3] = 'White'
game.board[1][4] = None
game.board[0][5] = None
game.board[6][3] = None
game.board[7][4] = None

for r in range(8):
  for c in range(8):
    print((r, c) if game.board[r][c] else '-----', end=" ")
  print("")
print("")
for r in range(8):
  for c in range(8):
    if game.board[r][c] == 'White':
      print('W', end=' ')
    elif game.board[r][c] == 'Black':
      print('B', end=' ')
    elif game.board[r][c] == 'Black_king':
      print('Bk', end=' ')
    elif game.board[r][c] == 'Black_Triple_King':
      print('B*', end=' ')
    elif game.board[r][c] == 'White_Triple_King':
      print('W*', end=' ')
    elif game.board[r][c] == 'White_king':
      print('Wk', end=' ')
    else:
      print('-', end=" ")
  print("")

print(
    game._get_moves((4, 1))
)

print(game._diagonal_coord((0, 0), (4, 4)))
