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

  def increment_captured_pieces_count(self, amount=1):
    """Increases the number of opponent pieces that the player has captured."""
    self.captured_pieces_count += amount


class Checkers:
  """The Checkers object represents the game as played.
  The class should contain information about the board and the players."""

  def __init__(self):
    # Initializing the board
    self.board = [[None for _ in range(8)] for _ in range(8)]
    # Initialize players
    self.players = [None, None]
    self.player_to_move_index = 0
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

  def create_player(self, player_name, piece_color):
    """Creates a player object with the given player_name and piece_color.
    The parameter piece_color is a string of value "Black" or "White" representing Black or White checkers pieces respectively.
    This function returns the player object that has been created."""
    if piece_color.lower() == 'black':
      index = 0
    else:
      index = 1
    p = Player(player_name, piece_color)
    self.players[index] = p

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

  def play_game(self, player_name, start, destination):
    """Makes a move with the given player_name, starting_square_location and destination_square_location of the piece.
    The square_location is a tuple in format (x,y).
    If a player attempts to move a piece out of turn, raise an OutofTurn exception.
    If the player_name is not valid, raise an InvalidPlayer exception.
    If a player does not own the checker present in the square_location or if the square_location does not exist on the baord; raise an InvalidSquare exception.
    This method returns the number of captured pieces, if any, otherwise return 0.
    If the destination piece reaches the end of opponent's side it is promoted as a king on the board. If the piece crosses back to its original side it becomes a triple king."""

    # Check if the start and destination squares are valid
    if not self._in_bound(start) or not self._in_bound(destination):
      raise InvalidSquare("Square location is not valid.")

    player_names = [(p.player_name if p else None) for p in self.players]
    if player_name not in player_names:
      raise InvalidPlayer("Player name is not valid.")

    # Check if it is the turn of the respective player
    if player_name != self.players[self.player_to_move_index].player_name:
      raise OutofTurn("It is not the turn of the respective player.")

    player = self.players[self.player_to_move_index]

    piece = self.get_checker_details(start)
    if piece == None or player.checker_color.lower() not in piece.lower():
      raise InvalidSquare(
          "Player does not own the checker present at the given square location.")

    # Get all valid moves for the given start location
    valid_moves = self._get_legal_moves(start)

    # Check if the destination square is one of the valid moves
    if destination not in [m[0] for m in valid_moves]:
      raise InvalidSquare("Invalid move.")

    curr_move = [m for m in valid_moves if m[0] == destination][0]
    is_capture = curr_move[1] == True

    # Move the piece
    captures, _promotion = self._play_move(start, destination, is_capture)
    capture_count = len(captures)
    player.increment_captured_pieces_count(capture_count)
    if _promotion:
      if 'ing' in _promotion:  # a king was promoted
        player.increment_triple_king_count()
      else:  # normal piece promotion
        player.increment_king_count()

    if is_capture:
      # check if the next move is a capture
      next_moves = self._get_legal_moves(destination)
      if next_moves and next_moves[0][1] == True:
        # continue capture
        return capture_count + self.play_game(player_name, destination, next_moves[0][0])

    # switch turn to next player
    self.player_to_move_index = (self.player_to_move_index + 1) % 2
    return capture_count

  # HELPER Methods

  def _get_legal_moves(self, square_location, check_best_capture=True):
    """Return all legal moves from a given square location"""
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
      bottom_left = self._get_valid_moves(bottom_left_squares, color, 0, 1)
      bottom_right = self._get_valid_moves(bottom_right_squares, color, 0, 1)
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

    # return the best capture move (maximum capture) if we have to
    if captures and check_best_capture:
      max_captures = self._get_max_capture_moves(square_location)
      return [(move[0], True) for move in max_captures]

    return captures or moves

  def _get_max_capture_moves(self, square_location):
    """Return the capture moves that would lead to a maximum capture from given square location"""
    moves = self._get_legal_moves(square_location, False)
    if not moves or moves[0][1] == False:
      # moves are not captures
      return [(None, 0)]

    captures = []
    max_capture_count = -1
    for move, is_capture in moves:
      # do move
      pieces, promotion = self._play_move(square_location, move, is_capture)
      captured_count = len(pieces)
      next_best = self._get_max_capture_moves(move)[0]
      captured_count += next_best[1]
      # undo move
      self._undo_play_move(square_location, move, pieces, promotion)
      captures += [(move, captured_count)]
      max_capture_count = max(max_capture_count, captured_count)

    return [move for move in captures if move[1] == max_capture_count]

  def _play_move(self, start, destination, is_capture):
    """Play a move on the board, move piece at start location to destination and return all pieces captured"""
    piece = self.board[start[0]][start[1]]
    self.board[destination[0]][destination[1]] = piece
    self.board[start[0]][start[1]] = None
    # capture checkers
    captured = []
    if is_capture:
      for coord in self._diagonal_coord(start, destination):
        captured_checker = self.get_checker_details(coord)
        if captured_checker != None:
          captured += [(coord, captured_checker)]
          self.board[coord[0]][coord[1]] = None

    # Check for promotion
    promoted = None
    # Promote to King if the piece reaches opponent's edge
    if piece.lower() == 'white' and destination[0] == 0:
      self.board[destination[0]][destination[1]] = 'White_king'
      promoted = 'White'
    elif piece.lower() == 'black' and destination[0] == 7:
      self.board[destination[0]][destination[1]] = 'Black_king'
      promoted = 'Black'

    # Promote to Triple King if the piece returns to its original side
    if not self._is_triple_king(piece) and self._is_king(piece):
      if not self._is_black_piece(piece) and destination[0] == 0:
        self.board[destination[0]][destination[1]] = 'White_Triple_King'
        promoted = 'White_king'
      if self._is_black_piece(piece) and destination[0] == 7:
        self.board[destination[0]][destination[1]] = 'Black_Triple_King'
        promoted = 'Black_king'

    return captured, promoted

  def _undo_play_move(self, start, destination, captured_checkers, promoted):
    """Undo a played move on the board, return piece from destination to start location
      and place all captured checkers at their original positions"""
    self.board[start[0]][start[1]] = self.board[destination[0]][destination[1]]
    self.board[destination[0]][destination[1]] = None
    # restore checkers
    for checkers in captured_checkers:
      coord, piece = checkers
      self.board[coord[0]][coord[1]] = piece
    # undo promoted
    if promoted:
      self.board[start[0]][start[1]] = promoted

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
      elif not all_moves or friendly:
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
        if not self._in_bound((r, c)) or (r, c) == stop:
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


# game.board[3][4] = 'Black'
# game.board[4][1] = 'Black_king'
game.board[3][2] = 'White'
game.board[4][3] = 'White'
game.board[5][2] = 'White'
game.board[5][4] = 'White'
game.board[1][4] = None
game.board[2][5] = 'Black'
game.board[5][6] = 'White'
game.board[4][3] = 'White'
game.board[5][2] = 'Black_king'
game.board[6][3] = 'White'
game.board[0][1] = None
game.board[0][5] = None
# game.board[6][3] = None
game.board[7][4] = None

for r in range(8):
  for c in range(8):
    print((r, c) if game.board[r][c] else '-----', end=" ")
  print("")
print("")


def dump(title=""):
  if title:
    print(f"[{title.upper()}]:")
  for r in range(8):
    for c in range(8):
      if not game.board[r][c]:
        print('-', end=" ")
      elif game.board[r][c].lower() == 'white':
        print('W', end=' ')
      elif game.board[r][c].lower() == 'black':
        print('B', end=' ')
      elif game.board[r][c].lower() == 'black_king':
        print('Bk', end=' ')
      elif game.board[r][c].lower() == 'black_triple_king':
        print('B*', end=' ')
      elif game.board[r][c].lower() == 'white_triple_king':
        print('W*', end=' ')
      elif game.board[r][c].lower() == 'white_king':
        print('Wk', end=' ')
    print("")
  print('_______________')


print(
    game._get_legal_moves((4, 1))
)

dump('INIT')
# pieces = game._play_move((4, 1), (1, 4), True)
# dump('after capture')
# game._undo_play_move((4, 1), (1, 4), pieces)
# dump('undo capture')

M = game._get_legal_moves((5, 2))
print(M)

game.play_game('Lucy', (5, 2), (7, 4))

dump('POST-MOVE')
