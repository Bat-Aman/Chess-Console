class Bishop:

  def __init__(self, row, col, player_num):
    self.row = row
    self.col = col
    self.symbol = ' B '
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
    if((curr_row == dest_row) and (curr_col == dest_col)):
      return False
    
    if(curr_row < dest_row):
      start_rowIndex = curr_row + 1
      stop_rowIndex = dest_row
      start_colIndex = curr_col
      stop_colIndex = dest_col
      is_from_row = 1

    else:
      chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
      if(piece_num != self.player_num):
        start_rowIndex = dest_row + 1
        stop_rowIndex = curr_row
        start_colIndex = dest_col
        stop_colIndex = curr_col
        is_from_row = 0
      else:
        return False
    
    if(start_colIndex < stop_colIndex):
      col_inc = 1
    else:
      col_inc = -1
    start_colIndex = start_colIndex + col_inc
    breakPoint = 0

    while(start_rowIndex <= stop_rowIndex):
      chess_piece, piece_num = piece_positions.get_piece(start_rowIndex, start_colIndex)
      if(piece_num != ' X  ' or start_colIndex == stop_colIndex):
        breakPoint = 1
        break
      start_rowIndex += 1
      start_colIndex += col_inc
    
    if(not breakPoint):
      start_rowIndex -= 1
      start_colIndex += (-col_inc)
    
    if(start_rowIndex != stop_rowIndex):
      return False
    
    if(start_colIndex != stop_colIndex):
      return False
    
    else:
      if(piece_num == ' X  '):
        return True
      
      if(is_from_row):
        if(piece_num != self.player_num):
          return True
        else:
          return False
      
      else:
        if(piece_num == self.player_num):
          return True
        else:
          return False