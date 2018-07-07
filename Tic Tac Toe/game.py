# source code

import random, os, time, sys, msvcrt


# main code
def main():
    # main screen 1
    os.system('mode con: cols=60 lines=25')
    os.system('color 1f')
    print('\n'*10)
    print('T I C  T A C  T O E'.center(60))
    time.sleep(2)

    # main screen 2
    os.system('cls')
    os.system('color 3f')
    print('\n'*10)
    print('--< Press 1 to 9 for X on Spaces >--'.center(60))
    time.sleep(4)

    # main screen 3
    os.system('cls')
    moves = 0
    board = newBoard()
    _level_(board, moves)
    

def _level_(board, moves): 
    while True:
        printBoard(board)
        move = msvcrt.getwch()
        moves += 1
        if move == '-': sys.exit()
        elif move == '+': main()
        else: move = int(move)
        
        if isFreeSpace(board, move):
            board[move] = 'X'
        else:
            os.system('cls')
            continue
        
        if result(board, 'X') == 'X':
            os.system('cls')
            printBoard(board)
            time.sleep(1)
            displayResult('win', moves)
            playAgain()
        
        board[getComputerMove(board)] = 'O'
            
        if result(board, 'O') == 'O':
            os.system('cls')
            printBoard(board)
            time.sleep(1)
            displayResult('lose', moves)
            playAgain()

        if isBoardFull(board):
            os.system('cls')
            printBoard(board)
            time.sleep(1)
            displayResult('tie', moves)
            playAgain()
        os.system('cls')


def newBoard():
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    return board


def printBoard(bd):
    os.system('cls')
    print('\n'*6)
    print((bd[7] + ' | ' + bd[8] + ' | ' + bd[9]).center(60))
    print((' ' + ' | ' + ' ' + ' | ' + ' ').center(60))
    print(('---+---+---').center(60))
    print((' ' + ' | ' + ' ' + ' | ' + ' ').center(60))
    print((bd[4] + ' | ' + bd[5] + ' | ' + bd[6]).center(60))
    print((' ' + ' | ' + ' ' + ' | ' + ' ').center(60))
    print(('---+---+---').center(60))
    print((' ' + ' | ' + ' ' + ' | ' + ' ').center(60))
    print((bd[1] + ' | ' + bd[2] + ' | ' + bd[3]).center(60))


def result(bd, le):
    if bd[1] == le and bd[2] == le and bd[3] == le:
        return le
    elif bd[4] == le and bd[5] == le and bd[6] == le:
        return le
    elif bd[7] == le and bd[8] == le and bd[9] == le:
        return le
    elif bd[1] == le and bd[4] == le and bd[7] == le:
        return le
    elif bd[2] == le and bd[5] == le and bd[8] == le:
        return le
    elif bd[3] == le and bd[6] == le and bd[9] == le:
        return le
    elif bd[1] == le and bd[5] == le and bd[9] == le:
        return le
    elif bd[3] == le and bd[5] == le and bd[7] == le:
        return le

def freeSpaceList(bd):
    lst = []
    for i in range(1, 10):
        if bd[i] == ' ':
            lst.append(i)
    return lst

def isFreeSpace(bd, move):
    if bd[move] == ' ':
        return 1
    else:
        return 0

def chooseRandomMove(bd, movesList):
    possibleMoves = []
    for i in movesList:
        if isFreeSpace(bd, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
        
def getBoardCopy(bd):
    dupeBoard = {}
    for k in bd:
        dupeBoard[k] = bd[k]
    return dupeBoard

def isBoardFull(bd):
    for i in bd:
        if bd[i] == ' ':
            return 0
    return 1

def displayResult(status, moves):
    if status == 'win':
        os.system('cls')
        os.system('color 2f')
        print('\n'*10)
        print(('You Won!! in '+str(moves)+' moves').center(60))
        time.sleep(2)
    elif status == 'lose':
        os.system('cls')
        os.system('color Cf')
        print('\n'*10)
        print('You Lose!! '.center(60))
        time.sleep(2)
    elif status == 'tie':
        os.system('cls')
        os.system('color Cf')
        print('\n'*10)
        print('Its a Tie!! '.center(60))
        time.sleep(2)
    playAgain()


def playAgain():
    os.system('cls')
    os.system('color 9f')
    print('\n'*10)
    print('Wanna Play Again: y|n'.center(60))
    inp = msvcrt.getwch()
    if inp.lower() == 'y': main()
    else: sys.exit()


#algorithm for tic tac toe AI

def getComputerMove(bd):
    #check if AI can win in next move
    for i in range(1, 10):
        copy = getBoardCopy(bd)
        if isFreeSpace(copy, i):
            copy[i] = 'O'
        if result(copy, 'O') == 'O':
            return i

    #check if player could win in next turn
    for i in range(1, 10):
        copy = getBoardCopy(bd)
        if isFreeSpace(copy, i):
            copy[i] = 'X'
        if result(copy, 'X') == 'X':
            return i

    #try to take corners, if its free
    move = chooseRandomMove(bd, [1, 3, 7, 9])
    if move != None:
        return move

    #try to take center, if its free
    if isFreeSpace(bd, 5):
        return 5

    #move on one of the sides
    return chooseRandomMove(bd, [2, 4, 6, 8])



if __name__ == '__main__':
    main()

        
