class Rook:
  
  def __init__(self, row, col, player_num):
    self.row = row
    self.col = col
    self.first_move = 1
    self.symbol = ' R '
    self.player_num = player_num

  def get_currPosition(self):
    return(self.row, self.col)
  
  def get_symbol(self):
    return(self.symbol)
  
  def get_playerNumber(self):
    return(self.player_num)
  
  def update_firstMove(self):
    self.first_move = 0
  
  def move(self, dest_row, dest_col):
    self.row = dest_row
    self.col = dest_col
    if(self.first_move):
      self.update_firstMove()

  def move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col):
    
    #   Check if move is column-wise
    if((curr_row == dest_row) and (curr_col != dest_col)):
      is_rowMove = 0
      backward_move = 0

      #Forward Move:
      if(curr_col < dest_col):
        start_index = curr_col + 1
        stop_index = dest_col
      
      #Backward Move:
      elif(curr_col > dest_col):
        chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
        if(self.player_num != piece_num):
          start_index = dest_col + 1
          stop_index = curr_col
          backward_move = 1
        else:
          return False
      
      else:
          return False
    
    # Check if move is row-wise:
    if((curr_row != dest_row) and (curr_col == dest_col)):
      is_rowMove = 1
      backward_move = 0

      #Forward Move:
      if(curr_row < dest_row):
        start_index = curr_row + 1
        stop_index = dest_row
      
      #Backward Move:
      elif(curr_col > dest_col):
        chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
        if(self.player_num != piece_num):
          start_index = dest_col + 1
          stop_index = curr_col
          backward_move = 1
        else:
          return False
      
      else:
          return False
    
    else:
      return False
    
    while(start_index <= stop_index):
      if(is_rowMove):
        chess_piece, piece_num = piece_positions.get_piece(start_index, curr_col)
      else:
        chess_piece, piece_num = piece_positions.get_piece(curr_row, start_index)
      
      if(piece_num != ' X  '):
        break
      start_index = start_index + 1
    
    if(start_index < stop_index):
      return False
    
    if(backward_move):
      if(piece_num == self.player_num):
        return True
      else:
        return False
    
    else:
      if(piece_num != self.player_num):
        return True
      else:
        return False