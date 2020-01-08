#noah hancock
# Tic Tac Toe
# 11/11/19

#Global constants
X="X"
O="O"
NUM_SQUARS= 9
TIE= "TIE"
EMPTY= " "

#working
def instructions():
    """Display game instructions"""
    print(
        """
    Welcome to the game called Tic-Tac-Toe.

    you will make your move by entering a number, 1-9. The number
    will correspond to the board poition as illustrated:

                   1 | 2 | 3 |
                   -----------
                   4 | 5 | 6 |
                   -----------
                   7 | 8 | 9 |

    good luck trying to beat me at tic tac toe. \n
    """
    )

#working
def ask_yes_no(question):
    """Ask a yes or no question. And give a one letter response back"""
    response= None
    while response not in ("y", "n", "yes", "no"):
        response= input(question).lower()
    x= response[0]
    return x
#x= ask_yes_no("is this going to work\n")
#print(x)

#working
def new_board():
    board= []
    for i in range(NUM_SQUARS):
        board.append(EMPTY)
    return board
#working
def display_board(board):
    print(str.format("""

 {0} | {1} | {2}
 ---------
 {3} | {4} | {5}
 ---------
 {6} | {7} | {8}
""",board[0],board[1],board[2],
             board[3],board[4],
             board[5],board[6],
             board[7],board[8]))
#working
def pieces():
    go_first= ask_yes_no("do you want the first move? (y/n): ")
    if go_first == "y":
        print("\n great then take your first move.")
        human = X
        comp= O
    else:
        print(" Sweet! i get the first move.")
        comp= X
        human= O
    return comp,human
#working
def ask_number(question, low, high):
    response= None
    while response not in range(low,high):
        try:
            response = int(input(question))
        except:
            print("Thats no a number")
            
    return response
#working
def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARS):
        if board[square]== EMPTY:
            moves.append(square)
    return moves


def human_move(board, human):
    legal= legal_moves(board)
    move= None
    while move not in legal:
        move= ask_number("where will you move (1-9): ",1, NUM_SQUARS+1)-1
        if move not in legal:
            print("\nSorry human but that square is already used. pick a diffrent spot\n")
    print("good spot")
    return move
#working
def next_turn(turn):
    if turn== X:
        return O
    else:
        return X

def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN= ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner= board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
        return None

def congrat_winner(winner, human, comp):
    if winner!= TIE:
          print(winner,"is the winner")      
    else:
        print(" Tie Game.")
    if winner== comp:
        print("I won! thanks for playing with me")
    elif winner==human:
        print(" congrats on winning. You were very good.")
    elif winner== TIE:
        print("I guess we tied huh. well congrats.")

def comp_move(board,human,comp):
    board_copy=board[:]
    BEST_MOVES=(0,6,8,2,4,1,7,3,5)
    print("I shall take square number", end=" ")
    for move in legal_moves(board):
        board_copy[move]=comp
        if winner(board_copy)==comp:
            print(move)
            return move
        board_copy[move]= EMPTY
        
    for move in legal_moves(board):
        board_copy[move]=human
        if winner(board_copy)==human:
            print(move)
            return move
        board_copy[move]= EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def tic_tac_toe():
    instructions()
    comp,human= pieces()
    board= new_board()
    turn= X
    display_board(board)
    win = None
    while win == None:
        if turn == human:
            move = human_move(board,human)
            board[move]=human
        else:
            move= comp_move(board,human,comp)
            board[move]=comp  
        display_board(board)
        turn = next_turn(turn)
        win = winner(board)
    congrat_winner(win,human,comp)
    input("press enter to return")


    
