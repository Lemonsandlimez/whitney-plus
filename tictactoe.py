import copy

print("x <-> , y ^v")
board = [["~", "~", "~"],
          ["~", "X", "~"],
          ["~", "~", "~"]]

def print_board(board):
    print("  1 2 3")  # column numbers
    for idx, row in enumerate(board, start=1):
        print(idx, "|".join(row))

def check_win(board, flip=True):
    winner = None
    for i in board:
        i = list(i)
        if i==list("X"*3):
            winner = "X"
        elif i==list("O"*3):
            winner = "O"

    if flip:
        swapped = list(zip(*board))
        #print_board(swapped)
        vertical_winner = check_win(swapped, False)
        if vertical_winner:
            return vertical_winner

    if check_diagonal("X"):
        return "X"
    elif check_diagonal("O"):
        return "O"
    return winner
    
def check_diagonal(symbol):
    return (all([board[0][0]==symbol, board[1][1]==symbol, board[2][2]==symbol])) or (all([board[0][2]==symbol, board[1][1]==symbol, board[2][0]==symbol]))
def check_move(x, y, board=board):
    if x>=0 and x<3 and y>=0 and y<3:
        #print(board[y][x])
        return board[y][x] == "~"
    else:
        return False

def cpu_move(user_x, user_y, board):
    ez_moves = [[2,2], [0,1], [2,1], [0,2], [2,2], [1,1], [0,0], [1,0], [1,2], [1,0]]

    for i in ez_moves:
        temp_board = copy.deepcopy(board)
        if check_move(i[0], i[1]):
            temp_board[i[1]][i[0]] = "X"

            if check_win(temp_board) == "X":
                print("CPU won using preliminary win analysis.")
                return temp_board
            else:
                del temp_board
    
    if check_move(user_x - 1, user_y, board) and board[user_x - 1][user_y] == "~": # AND shouldn't be needed, but it is.
        #print("x-1")
        #print(board[user_x - 1][user_y])
        board[user_x - 1][user_y] = "X"

    elif check_move(user_x + 1, user_y, board) and board[user_x - 1][user_y] == "~":
        #print("x+1")
        #print(board[user_x + 1][user_y])
        board[user_x + 1][user_y] = "X"

    elif check_move(2, 2): # One down from center
        board[2][2] = "X"

    elif check_move(0, 1): # One to the left of center
        board[1][0] = "X"

    elif check_move(2, 1): # One to the right of center
        board[1][2] = "X"

    elif check_move(0, 2): # Diagonal strategy 1
        board[2][0] = "X"

    elif check_move(1,1): # Diagonal strategy 2
        board[1][1] = "X"

    elif check_move(0,0): # Diagonal strategy 3
        board[0][0] = "X"

    elif check_move(1, 0): # One up from center
        board[0][1] = "X"


    elif check_move(1, 2): # The user is trying to force an easy draw. Maybe it was an accident?
        board[2][1] = "X"
        print("Drawed. Good Job!")

    elif check_move(1,0): # OK, that didn't work. CPU is probably doomed, but pretend to be confident.
        print("Oof.. uhh")
        board[0][1] = "X"

    else:
        print("Drawed. Good job!")
        return None
        

    return board

def check_tie(board):
    for i in board:
        if "~" in i:
            return False
    return True
        
print("Whitney+ is playing as X.")

print_board(board)
running = True

while running:
    data = input("Enter pos (x, y): ")
    # Split by comma and clean up spaces
    output = [item.strip() for item in data.split(',')]

    # Convert to integer FIRST, then subtract the offset
    x = int(output[0]) - 1
    y = int(output[1]) - 1
    
    if check_move(x, y):
        board[y][x] = "O"

        if check_win(board):
            print("Player", check_win(board), "won!")
            running = False
        
        print("CPU turn!")
        next_move = cpu_move(y, x, board)
        if next_move:
            board = next_move
            print_board(board)
        else:
            running = False
            print_board(board)

        
    else:
        print("Illegal move. Try again.")

    #print(check_win(board))
    #print_board(board)

    
    

    if check_win(board):
        print("Player", check_win(board), "won!")
        running = False
    elif check_tie(board):
        print("Both players are tied.")
        running = False
