#define board

from .pieces import p, r, n, b, q, k, P, R, N, B, Q, K
from .utils import coords_to_index

#class for the game board
class board:   
    def __init__(self, color=True):
        self.color = color 
        # set white side
        self.white = [P(['a', 2]), P(['b', 2]), P(['c', 2]), P(['d', 2]), P(['e', 2]), P(['f', 2]), P(['g', 2]), P(['h', 2]), 
        R(['a', 1]), N(['b', 1]), B(['c', 1]), Q(['d', 1]), K(['e', 1]), B(['f', 1]), N(['g', 1]), R(['h', 1])]
        # set the black side
        self.black = [p(['a', 7]), p(['b', 7]), p(['c', 7]), p(['d', 7]), p(['e', 7]), p(['f', 7]), p(['g', 7]), p(['h', 7]), 
        r(['a', 8]), n(['b', 8]), b(['c', 8]), q(['d', 8]), k(['e', 8]), b(['f', 8]), n(['g', 8]), r(['h', 8])]
        # set the initial board 
        self.board = [
            ['8  '] + self.black[8:16],
            ['7  '] + self.black[0:8],
            ['6  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['5  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['4  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['3  ', '. ', '. ', '. ', '. ' , '. ', '. ', '. ', '. '],
            ['2  '] + self.white[0:8],
            ['1  '] + self.white[8:16],
            ['', '', '', '', '', '', '', ''],
            ['   ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h']
        ]

    # return list of valid moves for current turn
    def get_valid_moves(self, turn):
        valid_moves = []
        for piece in (self.white if turn else self.black):
            valid_moves += [[piece.position, x] for x in piece.get_valid_moves(self, piece.position)]
        return valid_moves
    
    # draw board
    def draw(self):
        for row in self.board:
            for piece in row:
                if self.color:
                    if piece in self.white:
                        print(f'\033[30;107m{piece}\033[0m', end='')
                    else:
                        print(f'\033[40;97m{piece}\033[0m', end='')
                else:
                    print(piece, end='')
            print()
    
    # update the board matrix when a move is determined to be valid
    def update_board(self, current, new):
        cx, cy = current
        nx, ny = new
        current_location = self.board[cy][cx]
        new_location = self.board[ny][nx]
        if new_location != '. ':
            if new_location in self.white:
                self.white.remove(new_location)
            elif new_location in self.black:
                self.black.remove(new_location)
            new_location = '. '
        self.board[ny][nx] = current_location
        self.board[cy][cx] = new_location
        self.draw()

