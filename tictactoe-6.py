import turtle
import random

allowedToDraw = False
clickHappened = False
restartClick = False

# board is stored as a list
board = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
# E is empty, X and O are computer and player


def drawGrid(x, y):
    # draws grid in shape of # at x,y coordinates
    turtle.up()
    turtle.goto(x - 50, y - 150)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(300)
    turtle.backward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.backward(300)
    turtle.up()


def drawClick(x, y):
    global allowedToDraw
    global board
    global clickHappened
    clickHappened = True
    # draws circle at x,y coordinates
    # only draw if its players turn and in bounds and in an empty square
    inBounds = checkPlacePos(x, y)[0]
    emptySquare = checkPlacePos(x, y)[1]
    if allowedToDraw and inBounds and emptySquare:
        turtle.up()

        turtle.goto(
            spotLocation(checkPlacePos(x, y)[2])[0] + 64,
            spotLocation(checkPlacePos(x, y)[2])[1] + 34,
        )
        turtle.setheading(90)
        turtle.down()
        turtle.color("blue")
        turtle.circle(30)
        turtle.color("black")
        board[checkPlacePos(x, y)[2]] = "O"
    global restartClick
    if restartClick:
        board = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
        restartClick = False
        eraseAll(x, y)
        startGame(0, 0)


def checkPlacePos(x, y):
    global board
    # makes sure player doesnt place out of bounds or in a populated square
    emptySquare = False
    inBounds = True
    square = 0

    if x < -150 or x > 150 or y > 150 or y < -150:
        inBounds = False

    if y < 50:
        square += 3
    if y < -50:
        square += 3
    if x > -50:
        square += 1
    if x > 50:
        square += 1

    if board[square] == "E":
        emptySquare = True

    return inBounds, emptySquare, square


def drawX(x, y):
    # draws red X at x,y coordinates
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.color("red")
    turtle.pendown()
    turtle.right(45)
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(45)
    turtle.penup()
    turtle.color("black")


#################################
def draw_horizontal_line(x, y):

    turtle.penup()
    turtle.goto(x - 160, y + 50)
    turtle.setheading(90)
    turtle.speed(1)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(300)
    turtle.backward(300)
    turtle.right(180)
    turtle.penup()
    turtle.speed(0)


#################################
def draw_vertical_line(x, y):

    turtle.penup()
    turtle.goto(x - 130, y + 50)
    turtle.setheading(90)
    turtle.speed(1)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(300)
    turtle.penup()
    turtle.speed(0)


#################################
def draw_left_angle_line(x, y):
    turtle.penup()
    turtle.goto(x - 170, y + 50)
    turtle.setheading(90)
    turtle.speed(1)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(400)
    turtle.penup()
    turtle.speed(0)


##################################
def draw_right_angle_line(x, y):
    turtle.penup()
    turtle.goto(x - 170, y + 50)
    turtle.setheading(90)
    turtle.speed(1)
    turtle.pendown()
    turtle.left(0)
    turtle.left(135)
    turtle.forward(400)
    turtle.penup()
    turtle.speed(0)


def erasePrevious(x, y):
    # replaces an area with a white square to erase it
    y = y + 270
    turtle.color("white")
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(1000)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()


def eraseAll(x, y):
    # replaces everything with a white square to erase it
    y = y + 270
    turtle.color("white")
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.forward(1000)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(5000)
    turtle.right(90)
    turtle.forward(2000)
    turtle.right(90)
    turtle.forward(10000)
    turtle.right(90)
    turtle.forward(2000)
    turtle.right(90)
    turtle.forward(5000)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()


def playerTurn(x, y):

    erasePrevious(x, y)

    global allowedToDraw
    global clickHappened
    global restartClick
    turtle.up()
    turtle.goto(x, y + 250)
    turtle.down()
    # writes "player's turn", "click on a spot"
    turtle.write("Player's turn", align="center", font=("Arial", 32))
    turtle.up()
    turtle.goto(x, y + 200)
    turtle.down()
    turtle.write("Click to place a circle", align="center", font=("Arial", 20))
    turtle.penup()
    # waits until player clicks to end player turn
    allowedToDraw = True
    clickHappened = False
    while clickHappened == False:
        turtle.right(1)
    allowedToDraw = False


def computerTurn(x, y):
    global spot
    spotEmpty = False
    erasePrevious(x, y)

    # writes "computer's turn"
    turtle.up()
    turtle.goto(x, y + 250)
    turtle.down()
    turtle.write("Computer's turn", align="center", font=("Arial", 32))

    # waits ~2 seconds
    for i in range(random.randint(50, 125)):
        turtle.right(1)

    # computer decides where to place
    for i in range(9):
        spot = ""
        boardTest = board.copy()
        # checks if it can win next turn and chooses that spot
        if boardTest[i] == "E":
            boardTest[i] = "X"
            if aiWinnerCheck(boardTest) == "playerLose":
                spot = i
                spotEmpty = True
                break
        boardTest = board.copy()
        # checks if player can win next turn and chooses the spot that will block the player from winning (50% chance)
        if random.randint(0, 1) == 1:
            if boardTest[i] == "E":
                boardTest[i] = "O"
                if aiWinnerCheck(boardTest) == "playerWin":
                    spot = i
                    spotEmpty = True
                    break
    # otherwise take random spot until its open

    while not spotEmpty:
        randomSpot = random.randint(0, 8)
        if board[randomSpot] == "E":
            spot = randomSpot
            spotEmpty = True
            break


def aiWinnerCheck(board):
    # check if O wins
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        return "playerWin"

    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        return "playerWin"

    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        return "playerWin"

    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        return "playerWin"

    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        return "playerWin"

    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        return "playerWin"

    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        return "playerWin"

    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        return "playerWin"

    # check if X wins

    if board[1 - 1] == "X" and board[2 - 1] == "X" and board[3 - 1] == "X":
        return "playerLose"

    if board[4 - 1] == "X" and board[5 - 1] == "X" and board[6 - 1] == "X":
        return "playerLose"

    if board[7 - 1] == "X" and board[8 - 1] == "X" and board[9 - 1] == "X":
        return "playerLose"

    if board[1 - 1] == "X" and board[5 - 1] == "X" and board[9 - 1] == "X":
        return "playerLose"

    if board[3 - 1] == "X" and board[5 - 1] == "X" and board[7 - 1] == "X":
        return "playerLose"

    if board[1 - 1] == "X" and board[4 - 1] == "X" and board[7 - 1] == "X":
        return "playerLose"

    if board[2 - 1] == "X" and board[5 - 1] == "X" and board[8 - 1] == "X":
        return "playerLose"

    if board[3 - 1] == "X" and board[6 - 1] == "X" and board[9 - 1] == "X":
        return "playerLose"

    # if there are no winners check if there are any empty spaces, if not then a tie
    emptyFound = False
    for i in range(0, 8):
        if board[i] == "E":
            emptyFound = True
    if emptyFound == False:
        return "tie"

    # if no winners and empty spaces, return none
    return "none"

    # returns "playerWin", "playerLose", "tie", or "none"


def winnerCheck(board):
    # check if O wins
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        draw_horizontal_line(10, 50)
        return "playerWin"

    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        draw_horizontal_line(10, -50)
        return "playerWin"

    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        draw_horizontal_line(10, -150)
        return "playerWin"

    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        draw_left_angle_line(20, 90)
        return "playerWin"

    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        draw_right_angle_line(300, 90)
        return "playerWin"

    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        draw_vertical_line(30, 90)
        return "playerWin"

    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        draw_vertical_line(130, 95)
        return "playerWin"

    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        draw_vertical_line(235, 90)
        return "playerWin"

    # check if X wins

    if board[1 - 1] == "X" and board[2 - 1] == "X" and board[3 - 1] == "X":
        draw_horizontal_line(10, 50)
        return "playerLose"

    if board[4 - 1] == "X" and board[5 - 1] == "X" and board[6 - 1] == "X":
        draw_horizontal_line(10, -50)
        return "playerLose"

    if board[7 - 1] == "X" and board[8 - 1] == "X" and board[9 - 1] == "X":
        draw_horizontal_line(10, -150)
        return "playerLose"

    if board[1 - 1] == "X" and board[5 - 1] == "X" and board[9 - 1] == "X":
        draw_left_angle_line(20, 90)
        return "playerLose"

    if board[3 - 1] == "X" and board[5 - 1] == "X" and board[7 - 1] == "X":
        draw_right_angle_line(300, 90)
        return "playerLose"

    if board[1 - 1] == "X" and board[4 - 1] == "X" and board[7 - 1] == "X":
        draw_vertical_line(30, 90)
        return "playerLose"

    if board[2 - 1] == "X" and board[5 - 1] == "X" and board[8 - 1] == "X":
        draw_vertical_line(130, 95)
        return "playerLose"

    if board[3 - 1] == "X" and board[6 - 1] == "X" and board[9 - 1] == "X":
        draw_vertical_line(235, 90)
        return "playerLose"

    # if there are no winners check if there are any empty spaces, if not then a tie
    emptyFound = False
    for i in range(0, 8):
        if board[i] == "E":
            emptyFound = True
    if emptyFound == False:
        return "tie"

    return "none"

    # returns "playerWin", "playerLose", "tie", or "none"


def spotLocation(spot):
    # finds the x and y coordinates of the spot on the board
    if spot < 3:
        y = 66
    elif spot < 6:
        y = -34
    else:
        y = -134
    if spot % 3 == 0:
        x = -136
    elif spot % 3 == 1:
        x = -34
    elif spot % 3 == 2:
        x = 66
    return x, y


def startGame(x, y):
    global board
    global restartClick
    restartClick = False
    # decide if player or computer will go first
    turnCount = random.randint(0, 1)
    drawGrid(x, y)
    board = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
    # while winnercheck() has no tie and no winner, have the next player go
    while True:
        turnCount += 1

        if winnerCheck(board) == "playerWin":
            # clears top of screen,writes player won, writes 'click to play again'
            erasePrevious(x, y)
            turtle.up()
            turtle.goto(x, y + 250)
            turtle.down()
            turtle.write("Player Wins", align="center", font=("Arial", 32))
            turtle.up()
            turtle.goto(x, y + 200)
            turtle.down()
            turtle.write("Click to play again", align="center", font=("Arial", 20))
            turtle.penup()
            restartClick = True
            while restartClick == True:
                turtle.right(1)
        if winnerCheck(board) == "playerLose":
            # clears top of screen, writes computer won, writes 'click to play again'
            erasePrevious(x, y)
            turtle.up()
            turtle.goto(x, y + 250)
            turtle.down()
            turtle.write("Computer Wins", align="center", font=("Arial", 32))
            turtle.up()
            turtle.goto(x, y + 200)
            turtle.down()
            turtle.write("Click to play again", align="center", font=("Arial", 20))
            turtle.penup()
            restartClick = True
            while restartClick == True:
                turtle.right(1)
        if winnerCheck(board) == "tie":
            # clears top of screen, writes tie, writes 'click to play again'
            erasePrevious(x, y)
            turtle.up()
            turtle.goto(x, y + 250)
            turtle.down()
            turtle.write("Tied", align="center", font=("Arial", 32))
            turtle.up()
            turtle.goto(x, y + 200)
            turtle.down()
            turtle.write("Click to play again", align="center", font=("Arial", 20))
            turtle.penup()
            restartClick = True
            while restartClick == True:
                turtle.right(1)

        if winnerCheck(board) == "none":
            if turnCount % 2 == 0:
                playerTurn(x, y)
            else:
                computerTurn(x, y)
                board[spot] = "X"
                drawX(spotLocation(spot)[0], spotLocation(spot)[1])


if __name__ == "__main__":
    turtle.hideturtle()
    turtle.speed(0)
    turtle.width(4)
    turtle.Screen().onclick(drawClick)
    startGame(0, 0)
