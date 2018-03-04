class Knight:

  def __init__(self, row, col, player_num):
    self.row = row
    self.col = col
    self.symbol = ' N '
    self.player_num = player_num

  def get_currPosition(self):
    return (self.row, self.col)
  
  def get_symbol(self):
    return self.symbol
  
  def get_playerNumber(self):
    return self.player_num

  def move(self, dest_row, dest_col):
    self.row = dest_row
    self.col = dest_col

  def move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col):
    chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
    if(piece_num == self.player_num):
      return False
    
    if((curr_col - 2 == dest_col) or (curr_col + 2 == dest_col)):
      if((curr_row - 1 == dest_row) or (curr_row + 1 == dest_row)):
        return True
    
    elif((curr_col - 1 == dest_col) or (curr_col + 1 == dest_col)):
      if((curr_row - 2 == dest_row) or (curr_row + 2 == dest_row)):
        return True
    
    else:
        return False