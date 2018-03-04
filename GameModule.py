from piecesPlacement import Pieces
from KnightModule import Knight
from RookModule import Rook
from BishopModule import Bishop
from QueenModule import Queen
from PawnModule import Pawn

class Game:

  QUEEN = 1
  BISHOP = 2
  KNIGHT = 3
  ROOK = 4

  chess_board = [
        [' R2 ', ' N2 ', ' B2 ', ' Q2 ',
        ' K2 ', ' B2 ', ' N2 ', ' R2 '],
        [' p2 ', ' p2 ', ' p2 ', ' p2 ',
         ' p2 ', ' p2 ', ' p2 ', ' p2 '],
        [' X  ', ' X  ', ' X  ', ' X  ',
         ' X  ', ' X  ', ' X  ', ' X  '],
        [' X  ', ' X  ', ' X  ', ' X  ',
         ' X  ', ' X  ', ' X  ', ' X  '],
        [' X  ', ' X  ', ' X  ', ' X  ',
         ' X  ', ' X  ', ' X  ', ' X  '],
        [' X  ', ' X  ', ' X  ', ' X  ',
         ' X  ', ' X  ', ' X  ', ' X  '],
        [' p1 ', ' p1 ', ' p1 ', ' p1 ',
         ' p1 ', ' p1 ', ' p1 ', ' p1 '],
        [' R1 ', ' N1 ', ' B1 ', ' Q1 ',
         ' K1 ', ' B1 ', ' N1 ', ' R1 ']
    ]
  
  ROWS = 7
  COLUMNS = 7

  whiteKing_onCheck = False
  blackKing_onCheck = False

  piece_positions = Pieces()

  def __init__(self):
    row_2 = 0             #FOR PLAYER 2
    row_1 = 7             #FOR PLAYER 1

    player_1 = 1
    player_2 = 2

    