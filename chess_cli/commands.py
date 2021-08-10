# file for the command line interface (cli)
from .utils import coords_to_index, get_location, get_path_between_points
from random import choice
import readline

# function to initiate a move
def move_piece(b, c, n):
    cx, cy = c
    piece = b.board[cy][cx]
    if piece.validate_move(b, c, n):
        b.update_board(c, n)
        return True
    return False

class game:
    def __init__(self, board):
        self.board = board
        self.white = True
    
    def cli(self):
        print()
        prompt = "White's move: " if self.white else "Black's move: "
        try:
            command = input(prompt).split()
        except (KeyboardInterrupt, EOFError):
            exit()
        print()

        if len(command) == 0:
            self.board.draw()
            return

        if command[0].startswith('m') and len(command) == 3:
            c = coords_to_index(list(command[1]))
            n = coords_to_index(list(command[2]))
            try:
                piece = get_location(self.board.board, c)
            except ValueError:
                print('Invalid coordinates')
                return

            # move piece and change turn
            if piece not in (self.board.white if self.white else self.board.black):
                print(f'You can only move a {"white" if self.white else "black"} piece')
                return
            try:
                if move_piece(self.board, c, n):
                    self.white = not self.white
                else:
                    print('Invalid move')
            except ValueError:
                print('Invalid coordinates')
                return

        elif command[0] == 'r':
            print('Playing random move\n')
            move = choice(self.board.get_valid_moves(self.white))
            move_piece(self.board, move[0], move[1])
            self.white = not self.white
        
        elif command[0] == 'path':
            print(get_path_between_points([8, 0], [1, 7]))

        elif command[0] == 'q':
            exit()
            
        else:
            print('Invalid command')
