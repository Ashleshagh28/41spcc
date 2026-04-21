import random
board = [" " for _ in range(9)]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
   
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def get_empty_positions():
    return [i for i in range(9) if board[i] == " "]
def ai_move():
    for pos in get_empty_positions():
        board[pos] = "O"
        if check_winner("O"):
            return
        board[pos] = " "
    for pos in get_empty_positions():
        board[pos] = "X"
        if check_winner("X"):
            board[pos] = "O"
            return
        board[pos] = " "
    if board[4] == " ":
        board[4] = "O"
        return
    corners = [0,2,6,8]
    empty_corners = [c for c in corners if board[c] == " "]
    if empty_corners:
        board[random.choice(empty_corners)] = "O"
        return

    board[random.choice(get_empty_positions())] = "O"
def player_move():
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move!")
        player_move()
def is_draw():
    return " " not in board

while True:
    print_board()
    player_move()
    if check_winner("X"):
        print_board()
        print("You win!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break
    
    ai_move()
    if check_winner("O"):
        print_board()
        print("AI wins!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break
