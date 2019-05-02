"""tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""
from __future__ import print_function

choices = []
checkturns = []
for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    a = '\n -----'
    a += '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|'
    a += ' -----'
    a += '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|'
    a += ' -----'
    a += '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|'
    a += ' -----\n'
    return a

while not winner :
    printBoard()

    if (len(checkturns) == 9 and winner == False):
        print("Both lost")
        break
    
    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
        checkturns.append(choice)
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()
if winner == True:
    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")