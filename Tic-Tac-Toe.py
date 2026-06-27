import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def board_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position!")
            elif board[move] != " ":
                print("Position already taken!")
            else:
                board[move] = "X"
                break
        except:
            print("Enter a valid number!")

def computer_move():
    available = []

    for i in range(9):
        if board[i] == " ":
            available.append(i)

    move = random.choice(available)
    board[move] = "O"

    print("Computer chose position", move + 1)

print("=== TIC TAC TOE AI ===")
print("You = X")
print("Computer = O")

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if board_full():
        print_board()
        print("Match Draw!")
        break

    computer_move()

    if check_winner("O"):
        print_board()
        print("🤖 Computer Wins!")
        break

    if board_full():
        print_board()
        print("Match Draw!")
        break