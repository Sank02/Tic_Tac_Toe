

arr = [["","", ""], ["","", ""], ["","", ""] ]
user = True


def game():
    global user
    
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))

    while(arr[row][col] == " "): 
        row = input("Enter row: ")
        col = input("Enter col: ")


    userSym = "X" if user else "O"
    arr[row][col] = userSym

    user = not user 

    res = isRow(userSym, arr, row, col)

    if(res == "Lose"): 
       res = isCol(userSym, arr, row, col)

    if(res == "Lose"): 
       res = isDiag(userSym, arr, row, col)

    if(res == "Lose"): 
       res = isDiagReverse(userSym, arr, row, col)

    print(arr)
    print("You " + res)
    
   
def isRow(user, arr, row, col):

    for i in range(3):
        if(arr[row][i] != user):
            return "Lose"

    return "Win"


   
def isCol(user, arr, row, col):

    for i in range(3):
        if(arr[i][col] != user):
            return "Lose"

    return "Win"

def isDiag(user, arr, row, col):

    for i in range(3):
        if(arr[i][i] != user):
            return "Lose"


    return "Win"

def isDiagReverse(user, arr, row, col):
    print("reverse entered")
    for i in range(3):
        print(f"Checking cell {2-i}, {2-i}")
        print(f"Cell value: {arr[2-i][2-i]}")
        if arr[2-i][2-i] != user:
            return "Lose"

    return "Win"

# // draW
# // FOR EVERT INPOUT YOU ARE CHECKIGNG RESULT

    

while(True):
    game()