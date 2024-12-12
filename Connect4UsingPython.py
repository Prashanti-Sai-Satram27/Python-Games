import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔷":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "⭕":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    ### Check horizontal spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y + 1] == chip and gameBoard[x][y + 2] == chip and gameBoard[x][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check vertical spaces
    for y in range(cols):
        for x in range(rows - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y] == chip and gameBoard[x + 2][y] == chip and gameBoard[x + 3][y] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check upper right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y - 1] == chip and gameBoard[x + 2][y - 2] == chip and gameBoard[x + 3][y - 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y + 1] == chip and gameBoard[x + 2][y + 2] == chip and gameBoard[x + 3][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False  

def coordinateParser(inputString):
    if len(inputString) != 2 or inputString[0] not in possibleLetters or not inputString[1].isdigit():
        print("Invalid input format. Please enter again.")
        return None
    coordinate = [None] * 2
    coordinate[1] = possibleLetters.index(inputString[0])
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(intendedCoordinate):
    return gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == ''

def gravityChecker(intendedCoordinate):
    for row in range(rows-1, -1, -1):
        if isSpaceAvailable([row, intendedCoordinate[1]]):
            return [row, intendedCoordinate[1]]
    return None

leaveLoop = False
turnCounter = 0

while not leaveLoop:
    printGameBoard()
    if turnCounter % 2 == 0:
        while True:
            spacePicked = input("\nChoose a space (e.g., A0): ")
            coordinate = coordinateParser(spacePicked)
            if coordinate:
                gravityPosition = gravityChecker(coordinate)
                if gravityPosition:
                    modifyArray(gravityPosition, '🔷')
                    break
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid input. Please try again.")
        winner = checkForWinner('🔷')
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), str(random.randint(0, 5))]
            cpuCoordinate = coordinateParser(cpuChoice)
            if cpuCoordinate:
                gravityPosition = gravityChecker(cpuCoordinate)
                if gravityPosition:
                    modifyArray(gravityPosition, '⭕')
                    break
        winner = checkForWinner('⭕')

    if winner:
        printGameBoard()
        break
    
    turnCounter += 1
