from RookModule import Rook
from BishopModule import Bishop


class Queen(Rook, Bishop):
  def __init__(self, row, col, player_num):
    Rook.__init__(self, row, col, player_num)
    self.symbol = ' Q '

  def move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col):
    if(Rook.move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col)):
      is_valid_rookMove = 1
    else:
      is_valid_rookMove = 0
    
    if(Bishop.move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col)):
      is_valid_bishopMove = 1
    else:
      is_valid_bishopMove = 0

    if(is_valid_rookMove or is_valid_bishopMove):
      return True
    else:
        return False      