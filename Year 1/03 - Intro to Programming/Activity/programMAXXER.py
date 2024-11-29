'''
Hangman
Battleships
Tic Tac Toe
'''

def getDisplayBoard(board) :
    iterate = 0

    print("      C 0 | C 1 | C 2")

    print("----------------------")

    for row in board :
        print(f"R {iterate} |", "   | ".join(row))
        print("----------------------")
        iterate += 1

def getPlayerCoord() :
    column = int(input("Enter column in 0, 1, or 2: "))
    row = int(input("Enter row in 0, 1, or 2: "))

    return row, column

def isValidMove(board, row, column) :
    return 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == " "

def updateBoard(board, row, column, player) :
    board[row][column] = player

def isPlayerWinner(board, player) :
    if [player, player, player] in board : return True

    if player == board[0][0] and player == board[1][0] and player == board[2][0] : return True
    if player == board[0][1] and player == board[1][1] and player == board[2][1] : return True
    if player == board[0][2] and player == board[1][2] and player == board[2][2] : return True

    if player == board[0][0] and player == board[1][1] and player == board[2][2] : return True
    if player == board[0][2] and player == board[1][1] and player == board[2][0] : return True

    return False

def isTie(board) :
    if " " in board[0] : return False
    if " " in board[1] : return False
    if " " in board[2] : return False
    return True

players = {
    0 : "X",
    1 : "Y",
    2 : "Z"
}

# Keep program running until exit
while True :
    # Keep track of current iteration, begin with 0
    currentIteration = 0

    # Announce game begin
    print("The game begins!")

    # Set the board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Display board
    getDisplayBoard(board)

    # Keep current game running until a player wins
    while True :
        # Set current player
        currentPlayer = players[currentIteration]

        # Announce player's turn
        print(f"Player {currentPlayer}'s turn!")

        # Get current coordinates
        currentCoord = getPlayerCoord()

        # If it's not a valid move, announce and reset loop
        if not isValidMove(board, currentCoord[0], currentCoord[1]) :
            print("Invalid move!")
            continue

        # Update board
        updateBoard(board, currentCoord[0], currentCoord[1], currentPlayer)

        # Announce updated board
        print("Updating board")

        # Display board
        getDisplayBoard(board)

        # Check if player is winner, if a player wins, break loop
        if isPlayerWinner(board, currentPlayer) :
            print("Player", currentPlayer, "won!")
            break

        # Check for tie condition, break loop if tie
        if isTie(board) :
            print("The game is a tie!")
            break

        # Iterate through players
        currentIteration += 1
        # Use a modulo to reset list
        currentIteration %= 3
    
    # Ask user if they want to exit
    if input("Type \"Exit\" to exit program or type anything to continue.").lower() == "exit" :
        print("Goodbye and have a nice day!")
        quit()