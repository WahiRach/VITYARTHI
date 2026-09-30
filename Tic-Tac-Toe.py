import random
Victory = [
    (0, 1, 2),  
    (3, 4, 5), 
    (6, 7, 8),  
    (0, 3, 6),  
    (1, 4, 7),  
    (2, 5, 8),  
    (0, 4, 8),  
    (2, 4, 6),  
]


def CreateBoard():
    return list("123456789")
def ShowBoard(board):#prints the board every round 
    print()
    print( board[0]," | ", board[1]," | ",board[2] )
    print("---+---+---")
    print( board[3]," | ",board[4]," | ", board[5])
    print("---+---+---")
    print(board[6]," | ",board[7]," | ", board[8] )
    print()

def Mode(): #2 modes
    while True:
        print("Game modes:")
        print("1. Two players")
        print("2. Play against the computer")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return "two players"
        if choice == "2":
            return "computer"


def PlayerMove(board, player): #takes the player square
    while True:
        move = input("Player choose a square (1-9): ").strip()

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        i= int(move) - 1
        if board[i] in ("X", "O"):
            print("That square already occupied. Choose another one.")
            continue

        return i


def ComputerTurn(board):# takes the computer square
    blank= []
    for i in range(len(board)):
        if board[i] not in ("X", "O"):
            blank.append(i)

    i= random.choice(blank)
    print("Computer chooses square ",i+ 1)
    return i


def Winning(board, player): #win position
    for j in Victory:
        first, second, third = j
        if board[first] == board[second] == board[third] == player:
            return True
    return False


def isFullOrNot(board):# draw position
    for i in board:
        if i not in ("X", "O"):
            return False
    return True


def SecondPlayer(player):#two player
    if player == "X":
        return "O"
    return "X"


def StartPlaying(mode):# play start
    board = CreateBoard()
    player = "X"

    print("Welcome to our Tic-tac-toe game!")
    print("Choose one of the squares by entering its number.")
    if mode == "computer":
        print("YOU: X -----------AND------------ COMPUTER: O")

    while True:
        ShowBoard(board)
        if mode == "computer" and player == "O":
            index = ComputerTurn(board)
        else:
            index = PlayerMove(board, player)

        board[index] = player

        if Winning(board, player):
            ShowBoard(board)
            if mode == "computer" and player == "O":
                print("-------YOU LOST!-----------")
            else:
                print("---PLAYER--",player,"--WINS--------")
            return

        if isFullOrNot(board):
            ShowBoard(board)
            print("The game is a draw!")
            return

        player = SecondPlayer(player)


def OneMoreTime():#play again
    while True:
        answer = input("Would you like to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with y or n.")


def main():
    while True:
        mode = Mode()
        StartPlaying(mode)

        if not OneMoreTime():
            return "Thanks for playing"

print(main())