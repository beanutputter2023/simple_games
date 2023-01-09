# printing the game board
board = [ "_" for x in range(9)]
currentPlayer = "x"
winner = None
gameRunning = True

def display():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

#taking user input
def userInput():
    while True:
        if currentPlayer == "x":
            n = int(input(" Player x's turn. Enter position (1-9):"))
        else:
            n = int(input("Player o's turn. Enter position (1-9):"))
        if n >= 1 and n <= 9 and board[n-1] == "_":
            board[n-1] = currentPlayer
            break
        else:
            if currentPlayer == "x":
                print("Oops! position unavailable. Try again Player x.")
            else:
                print("Oops! position unavailable. Try again Player o.")
            display()


# check for win or tie2
def checkHori():
    global winner
    if (board[0] == board[1] and board[0] == board[2] and board[0] != "_") or (board[3] == board[4] and board[3]== board[5] and board[3] != "_") or (board[6] == board[7] and board[6] == board[8] and board[6] != "_"):
        winner = currentPlayer
        return True
def checkVert():
    global winner
    if (board[0] == board[3] and board[0] == board[6] and board[0] != "_") or (board[1] == board[4] and board[1]== board[7] and board[1] != "_") or (board[2] == board[5] and board[2] == board[8] and board[2] != "_"):
        winner = currentPlayer
        return True
def checkDiag():
    global winner
    if (board[0] == board[4] and board[0] == board[8] and board[0] != "_") or (board[2] == board[4] and board[2]== board[6] and board[3] != "_"):
        winner = currentPlayer
        return True

def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

def checkWin():
    if checkHori() or checkVert() or checkDiag():
        print(f"The winner is {winner}.")

def checkTie():
    global gameRunning
    if "_" not in board:
        display()
        print("It's a tie.")
        gameRunning = False

while gameRunning:
    display()
    if winner != None:
        break
    userInput()
    checkWin()
    checkTie()
    switchPlayer()