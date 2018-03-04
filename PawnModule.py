class Pawn:

  def __init__(self, row, col, player_num):
    self.row = row
    self.col = col
    self.first_move = 1
    self.num_of_moves = 0
    self.symbol = ' P '
    self.player_num = player_num
  
  def get_currPosition(self):
    return(self.row, self.col)
  
  def get_symbol(self):
    return(self.symbol)
  
  def get_playerNumber(self):
    return(self.player_num)
  
  def update_firstMove(self):
    self.first_move = 0

  def promote_piece(self):
    if(self.player_num == 1  and self.row == 8):
      return True
    if(self.player_num == 2  and self.row == 1):
      return True
    else:
      return False
  
  def move_validation(self, piece_positions, curr_row, curr_col, dest_row, dest_col):
    if(self.player_num == 2):
      if(curr_col == dest_col):
        if(curr_row + 1 == dest_row):
          chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
          if(piece_num == ' X  '):
            return True
          else:
            return False
    
        elif(curr_row + 2 == dest_row  and first_move == 1):
          chess_piece_1, piece_num_1 = piece_positions.get_piece(curr_row + 1, curr_col)
          chess_piece_2, piece_num_2 = piece_positions.get_piece(curr_row + 2, curr_col)
          if(piece_num_1 == ' X  ' and piece_num_2 == ' X  '):
            return True
          else:
            return False
        else:
          return False

      
      elif(curr_row + 1 == dest_row):
        chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
        if((curr_col + 1 == dest_col) or (curr_col - 1 == dest_col)):
          if(piece_num == 1):
            return True
          else:
            return False
      else:
        return False


    if(self.player_num == 1):
      if(curr_col == dest_col):
        if(curr_row - 1 == dest_row):
          chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
          if(piece_num == ' X  '):
            return True
          else:
            return False
    
        elif(curr_row - 2 == dest_row  and first_move == 1):
          chess_piece_1, piece_num_1 = piece_positions.get_piece(curr_row - 1, curr_col)
          chess_piece_2, piece_num_2 = piece_positions.get_piece(curr_row - 2, curr_col)
          if(piece_num_1 == ' X  ' and piece_num_2 == ' X  '):
            return True
          else:
            return False
        else:
          return False

      
      elif(curr_row - 1 == dest_row):
        chess_piece, piece_num = piece_positions.get_piece(dest_row, dest_col)
        if((curr_col + 1 == dest_col) or (curr_col - 1 == dest_col)):
          if(piece_num == 1):
            return True
          else:
            return False
      else:
        return False

  def move(self, dest_row, dest_col):
    self.row = dest_row
    self.col = dest_col
    self.num_of_moves = num_of_moves + 1
    if(self.first_move):
      self.update_firstMove()
    


    
