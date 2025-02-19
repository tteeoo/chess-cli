# file containing functions used throughout the project

# take board x value and turn return a equivalent value for the matrix
def x_axis_to_index(x):
    if x == 'a': return 1
    if x == 'b': return 2
    if x == 'c': return 3
    if x == 'd': return 4
    if x == 'e': return 5
    if x == 'f': return 6
    if x == 'g': return 7
    if x == 'h': return 8

# take board y value and turn return a equivalent value for the matrix
def y_axis_to_index(y):
    y = int(y)
    if y == 1: return 7
    if y == 2: return 6
    if y == 3: return 5
    if y == 4: return 4
    if y == 5: return 3
    if y == 6: return 2
    if y == 7: return 1
    if y == 8: return 0

# take x and y and return corresponding indices
def coords_to_index(coords):
    return [x_axis_to_index(coords[0]), y_axis_to_index(coords[1])]

# get right up path
def right_up(board, c, distance):
    cx, cy = c
    return [board[cy-i-1][cx+i+1] for i in range(distance)]

# get right down path
def right_down(board, c, distance):
    cx, cy = c
    return [board[cy+i+1][cx+i+1] for i in range(distance)]


# get right path
def right(board, c, distance):
    cx, cy = c
    return [board[cy][cx+i+1] for i in range(distance)]

# get left path
def left(board, c, distance):
    cx, cy = c
    return [board[cy][cx-i] for i in range(1, distance+1)]

# get up path
def up(board, c, distance):
    cx, cy = c
    return [board[cy-i-1][cx] for i in range(distance)]

# get down path
def down(board, c, distance):
    cx, cy = c
    return [board[cy+i+1][cx] for i in range(distance)]

# get left up path
def left_up(board, c, distance):
    cx, cy = c
    return [board[cy-i][cx-i] for i in range(1, distance+1)]

# get left down path
def left_down(board, c, distance):
    cx, cy = c
    return [board[cy+i][cx-i] for i in range(1, distance+1)]

def get_path_between_points(c, n):
    cx, cy = c
    nx, ny = n
    if cx < nx and cy==ny: 
        return [[cx+i, cy] for i in range(nx-cx+1)]
    if cx > nx and cy == ny:
        return [[cx-i, cy] for i in range(cx-nx+1)]
    if cx == nx and cy > ny:
        return [[cx, cy-i] for i in range(cy-ny+1)]
    if cx == nx and cy < ny:
        return [[cx, cy+i] for i in range(ny-cy+1)]
    if cx < nx and cy > ny: 
        return [[cx+i, cy-i] for i in range(nx-cx+1)]
    if cx < nx and cy < ny: 
        return [[cx+i, cy+i] for i in range(nx-cx+1)]
    if cx > nx and cy > ny:
        return [[cx-i, cy-i] for i in range(cx-nx+1)]
    if cx > nx and cy < ny:
        return [[cx-i, cy+i] for i in range(cx-nx+1)]

# get valid moves vertical and horizontal (for rooks and queens)
def valid_vertical_horizontal_moves(b, c, side):
    valid_moves = []
    cx, cy = c
    board = b.board
    paths = [up(board, c, cy), down(board, c, 7-cy), right(board, c, 8-cx), left(board, c, cx-1)]
    for i in range(len(paths[0])):
        if paths[0][i] == '. ':
            valid_moves.append([cx, cy-i-1])
        elif paths[0][i] in side:
            break
        else:
            valid_moves.append([cx, cy-i-1])  
            break
    
    for i in range(len(paths[1])):
        if paths[1][i] == '. ':
            valid_moves.append([cx, cy+i+1])
        elif paths[1][i] in side:
            break
        else:
            valid_moves.append([cx, cy+i+1])  
            break

    for i in range(len(paths[2])):
        if paths[2][i] == '. ':
            valid_moves.append([cx+i+1, cy])
        elif paths[2][i] in side:
            break
        else:
            valid_moves.append([cx+i+1, cy])  
            break

    for i in range(1, len(paths[3])+1):
        if paths[3][i-1] == '. ':
            valid_moves.append([cx-i, cy]) 
        elif paths[3][i-1] in side:
            break
        else:
            valid_moves.append([cx-i, cy])  
            break
    
    return valid_moves

def valid_diagonal_moves(b, c, side):
    valid_moves = []
    cx, cy = c
    board = b.board
    dr, dl, down = 8-cx, cx-1, 7-cy
    drd, dld = dr, dl
    if cy < dr: dr = cy
    if cy < dl: dl = cy
    if down < drd: drd = down
    if down < dld: dld = down
    ru = right_up(board, c, dr)
    lu = left_up(board, c, dl)
    rd = right_down(board, c, drd)
    ld = left_down(board, c, dld)
    for i in range(len(ru)):
        if ru[i] == '. ':
            valid_moves.append([cx+1+i, cy-1-i])
        elif ru[i] in side:
            break
        else:
            valid_moves.append([cx+1+i, cy-1-i])
    for i in range(len(lu)):
        if lu[i] == '. ':
            valid_moves.append([cx-1-i, cy-1-i])
        elif lu[i] in side:
            break
        else:
            valid_moves.append([cx-1-i, cy-1-i])
    for i in range(len(ld)):
        if ld[i] == '. ':
            valid_moves.append([cx-1-i, cy+1+i])
        elif ld[i] in side:
            break
        else:
            valid_moves.append([cx-1-i, cy+1+i])
    for i in range(len(rd)):
        if rd[i] == '. ':
            valid_moves.append([cx+1+i, cy+1+i])
        elif rd[i] in side:
            break
        else:
            valid_moves.append([cx+1+i, cy+1+i])
    return valid_moves

# knight moves
# these functions return the pieces in each possible knight move
def l_up_right(board, c):
    cx, cy = c
    return [board[cy-2][cx-len(board[cy-2])+1], board[cy-1], [cx-len(board[cy-1])+2]]

def l_up_left(board, c):
    cx, cy = c
    return [board[cy-2][cx-1], board[cy-1][cx-2]]

def l_down_right(board, c):
    cx, cy = c
    return [board[cy+2][cx-len(board[cy+2])+1], board[cy+1], [cx-len(board[cy+1])+2]]

def l_down_left(board, c):
    cx, cy = c
    return [board[cy+2][cx-1], board[cy+1][cx-2]]

# get valid knight moves
def knight_logic(board, c, side):
    valid_moves = []
    b = board.board
    cx, cy = c
    if l_up_right(b, c)[0] not in side:
        valid_moves.append([cx+1, cy-2])
    if l_up_right(b, c)[1] not in side:
        valid_moves.append([cx+2, cy-1])
    if l_up_left(b, c)[0] not in side:
        valid_moves.append([cx-1, cy-2])
    if l_up_left(b, c)[1] not in side:
        valid_moves.append([cx-2, cy-1])
    if l_down_right(b, c)[0] not in side:
        valid_moves.append([cx+1, cy+2])
    if l_down_right(b, c)[1] not in side:
        valid_moves.append([cx+2, cy+1])
    if l_down_left(b, c)[0] not in side:
        valid_moves.append([cx-1, cy+2])
    if l_down_left(b, c)[1] not in side:
        valid_moves.append([cx-2, cy+1])
    return valid_moves

def king_logic(b, c, side):
    valid_moves = []
    cx, cy = c
    board = b.board
    u, d, r, l = up(board, c, 1)[0], down(board, c, 1)[0], right(board, c, 1)[0], left(board, c, 1)[0]
    if u == '. ' or u not in side:
        valid_moves.append([cx, cy-1])
    if d == '. ' or d not in side:
        valid_moves.append([cx, cy+1])
    if l == '. ' or l not in side:
        valid_moves.append([cx-1, cy])
    if r == '. ' or r not in side:
        valid_moves.append([cx+1, cy])
    ru, lu, rd, ld = right_up(board, c, 1)[0], left_up(board, c, 1)[0], right_down(board, c, 1)[0], left_down(board, c, 1)[0]
    if ru == '. ' or ru not in side:
        valid_moves.append([cx+1, cy-1])
    if lu == '. ' or lu not in side:
        valid_moves.append([cx-1, cy-1])
    if rd == '. ' or rd not in side:
        valid_moves.append([cx+1, cy+1])
    if ld == '. ' or ld not in side:
        valid_moves.append([cx-1, cy+1])
    return valid_moves

def get_location(b, c, pre_parsed=False):
    cx, cy = c
    if cx > 8 or cy > 7: return False
    if cx < 0 or cy < 0: return False
    return b[cy][cx] 

def check_detection(b, side):
    m = []
    board = b.board
    k = 'k ' if side == b.black else 'K '
    side = b.white if side == b.black else b.black
    for y in range(len(board)):
        for x in range (len(board[y])):
            p = board[y][x]
            if p in side:
                moves = p.get_valid_moves(b, p.position)
                pr = {'p': p, 'pos': coords_to_index(p.position), 'moves': []}
                for move in moves:
                    if str(get_location(b.board, move, pre_parsed=True)) == k: 
                        pr['moves'].append(move)
                if pr['moves'] != []:
                    m.append(pr)
    return m

def get_sides_valid_moves(b, side):
    moves = []
    board = b.board
    for y in range(len(board)):
        for x in range (len(board[y])):
            p = board[y][x]
            if p in side:
                moves.append(p.get_valid_moves(b, p.position))
    return moves

def check_mate_detection(b, side, opps):
    moves = []
    for p in opps:
        path = get_path_between_points(p['pos'], p['moves'][0])
        [moves.append(l) for l in path]
    # TODO get dictof piece and moves and if pieces moves are in path then they cna move there
    # not sure how to implement maybe special thing in game class idk its late
    return moves
