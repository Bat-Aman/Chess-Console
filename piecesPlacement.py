"""
Identification Rules for pieces:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The First letter represents the piece_name
2. Digit(1 or 2) represents the piece of player 1 or 2.
3. 1 -> Always White         &&     2 -> Always Black

* for example: *
P1 -> whitePawn    &&     P2 -> blackPawn
Nx -> Knight-----------
Bx -> Bishop           |
Qx -> Queen            |--------->   Here, 'x' is Player '1' or '2'
Kx -> King             | 
Rx -> Rook-------------

"""


class Pieces:
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

    row_label = range(8, 0, -1)
    column_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def print_board(self):
        print('')
        for i in self.chess_board:
            for j in i:
                print("|------|", end="")
            print()
            for j in i:
                print("|", j, "|", end="")
            print()
        print("|------|" * 8, end="")

    def get_piece(self, row, col):
        piece = self.chess_board[row][col]
        chess_piece = piece[0]
        piece_num = piece[1]
        if(piece_num != '-'):
            piece_num = int(piece_num)
        return (chess_piece, piece_num)

    def update_board(self, curr_row, curr_col, dest_row, dest_col):
        self.chess_board[curr_row][curr_col] = self.chess_board[dest_row][dest_col]
        self.chess_board[curr_row][curr_col] = ' X  '

    def replace_piece(self, piece, row, col):
        self.chess_board[row][col] = piece


def main():
    p = Pieces()
    p.print_board()


if __name__ == "__main__":
    main()
