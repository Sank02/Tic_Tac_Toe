

arr = [["", "", ""], ["", "", ""], ["", "", ""]]
chessBoardSize = 3  # 3x3
user = True
userSymbol = "X" if user else "O"

noOfMoves = 0


def game():

    while (True):
        result = playMove()

        if (result):
            if (result == True):
                print(userSymbol, "won the game")
            else:
                print(result)
            break


def playMove():
    global user
    global noOfMoves

    try:
        print("\n---------------", noOfMoves)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if (arr[row][col] == ""):
            userSymbol = "X" if user else "O"
            arr[row][col] = userSymbol
            noOfMoves += 1
            printChessBoard()
            user = not user

            return isCheckMate(row, col)

        else:
            print("This space is already filled. Please choose some other location.")

    except:
        print("Error Non numeric values not allowed. Only integers accepted.")


def printChessBoard():
    print(arr[0])
    print(arr[1])
    print(arr[2])


def isCheckMate(row, col):
    res = isRow(userSymbol, arr, row, col)

    if (res != True):
        res = isCol(userSymbol, arr, row, col)

    if (res != True & row == col):
        res = isDiag(userSymbol, arr)

    if (res != True & row == col):
        res = isDiagReverse(userSymbol, arr)

    if (res != True):
        gameOver = isMatchDrawn()
        if (gameOver):
            return "Match is drawn..."

    return res


def isMatchDrawn():
    if (noOfMoves > 7):
        return True
    else:
        return False


def isRow(userSymbol, arr, row, col):

    obj = {
        "X": 0,
        "O": 0
    }

    for i in range(chessBoardSize):
        if (arr[row][i] == "X"):
            obj["X"] += 1
        elif (arr[row][i] == "O"):
            obj["O"] += 1

    if (obj["X"] == chessBoardSize | obj["O"] == chessBoardSize):
        return True
    elif (obj["X"] + obj["O"] == chessBoardSize):
        return "Lose"
    else:
        return False


def isCol(userSymbol, arr, row, col):

    obj = {
        "X": 0,
        "O": 0
    }

    for i in range(chessBoardSize):
        if (arr[i][col] == "X"):
            obj["X"] += 1
        elif (arr[i][col] == "O"):
            obj["O"] += 1

    if (obj["X"] == chessBoardSize | obj["O"] == chessBoardSize):
        return True
    elif (obj["X"] + obj["O"] == chessBoardSize):
        return "Lose"
    else:
        return False


def isDiag(userSymbol, arr):

    obj = {
        "X": 0,
        "O": 0
    }

    for i in range(chessBoardSize):
        if (arr[i][i] == "X"):
            obj["X"] += 1
        elif (arr[i][i] == "O"):
            obj["O"] += 1

    if (obj["X"] == chessBoardSize | obj["O"] == chessBoardSize):
        return True
    elif (obj["X"] + obj["O"] == chessBoardSize):
        return "Lose"
    else:
        return False


def isDiagReverse(userSymbol, arr):

    obj = {
        "X": 0,
        "O": 0
    }

    for i in range(chessBoardSize):

        if (arr[2-i][2-i] == "X"):
            obj["X"] += 1
        elif (arr[2-i][2-i] == "O"):
            obj["O"] += 1

    if (obj["X"] == chessBoardSize | obj["O"] == chessBoardSize):
        return True
    elif (obj["X"] + obj["O"] == chessBoardSize):
        return "Lose"
    else:
        return False


# // FOR EVERT INPOUT YOU ARE CHECKIGNG RESULT
game()
