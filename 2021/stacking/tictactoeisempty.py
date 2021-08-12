from itertools import chain
from random import choice


def cast(x, y, base):
    """
    Create a y by x matrix from a vector
    """
    if x * y == len(base):
        return [list(base[i*x: x+i*x]) for i in range(y)]
    raise ValueError('Dimensions do not agree with base')

def flat(board):
    """
   Create a 1D vector from a matrix 
    """
    return [*chain.from_iterable(board)]

def check_space_taken(board, number):
    """
    check if a space is taken
    """
    return flat(board)[number] == ' '

def empty_space_indices(board):
    """
    find all empty spaces
    """
    flattened = flat(board)
    return [*filter(lambda x: flattened[x]==' ', range(len(flattened)))]

def play(board, number, letter):
    """
   Simplify the code base by using a single function for move-making 
    """
    board = flat(board)
    board[number] = letter
    board = cast(3, 3, board)
    return board

def won(board, letter):
    """
    checkwin seems to have a bug
    """
    for i in range(3):
        if letter == board[i][0] == board[i][1] == board[i][2]:
            return True
        elif letter == board[0][i] == board[1][i] == board[2][i]:
            return True
        elif letter == board[0][0] == board[1][1] == board[2][2]:
            return True
        elif letter == board[2][0] == board[1][1] == board[0][2]:
            return True
    return False

def show(board):
    """
    Neat representation of the board.
    checkout the module tabulate for better options:
        https://github.com/astanin/python-tabulate
    """
    table = '\n'.join("{}|{}|{}".format(*row) for row in board)
    table = table.join('\n' * 2)
    print(table)
    return table

def game_over(board):
    """
    check if the board is full or there is a winner
    """
    return len(empty_space_indices(board))==0 or won(board, 'x') or won(board, 'o')
    
def main(board=None):
    """REPL"""
    if board:
        show(board)
    board = board if not isinstance(board, type(None)) else [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    player_move = None
    while not game_over(board):
        while not player_move in empty_space_indices(board):
            player_move = int(input(f'pick a tile from {empty_space_indices(board)}:\n\t'))
        board = play(board, player_move, 'x')
        
        if not game_over(board):
            computer_move = choice(empty_space_indices(board))
            board = play(board, computer_move, 'o')
            
        show(board)

main()



def relist(table):
    """parse the table from show back into a list"""
    t = table.splitlines()
    return [i.split('|') for i in t]
    
t = """x|o|o
 |o|o
x|x|x"""
t = """x|o|o
 | |o
x|x|x"""
t = """x|o|
 | |o
x|o|x"""
rt = relist(t)
main(rt)

# for r in rt: print(r)
# print(checkwin(rt))
# print(game_over(rt))
# print(won(rt, 'x'))


