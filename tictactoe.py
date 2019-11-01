import random

def drawBoard(board):
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print('-------------')
    print(' '+board[4]+'|'+board[5]+'|'+board[6])
    print('-------------')
    print(' '+board[1]+'|'+board[2]+'|'+board[3])

def inputPlayerLetter():
    letter = ''
    while not(letter == "X" or letter == "O"):
        print("X or O")
        letter = input().upper()

    if letter == "X":
        return ['X','O']
    else:
        return ['O','X']

def duplicate(board):
    dup_board = []
    for i in board:
        dup_board.append(i)
    return dup_board

def RandomMove(board,movelist):
    possiblemove = []
    for i in movelist:
        if blank(board,i):
            possiblemove.append(i)
    if len(possiblemove) > 0:
        return random.choice(possiblemove)
    else:
        return None

def iswinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le))

def isfull(board):
    for i in range(1,10):
        if blank(board,i):
            return False
    return True
        

def ComputerMove(board,letter):
    if letter == "X":
        playerL = "O"
    else:
        playerL = "X"

    for i in range(1,10):
        copy = duplicate(board)
        if blank(copy,i):
            makeMove(copy,letter,i)
            if iswinner(copy,letter):
                return i
    for i in range(1,10):
        copy = duplicate(board)
        if blank(copy,i):
            makeMove(copy,playerL,i)
            if iswinner(copy,playerL):
                return i
    move = RandomMove(board,[1,3,7,9])
    if move != None:
        return move

    if blank(board,5):
        return 5

    return RandomMove(board,[2,4,6,8])

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def blank(board,move):
    return board[move].isdigit()

def makeMove(board,letter,move):
    if blank(board,move):
        board[move] = letter
    else:
        raise Exception("Field is occupied")

def Move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not blank(board,int(move)):
        print("Enter your move (1-9)")
        move = input()
    return int(move)
    
def main():
    print("Welcome to Tic Tac Toe")

    random.seed()
    while True:
        #Reset Board
        Board = ['']*10

        for i in range(9,0,-1):
            Board[i] = str(i)
        playerLetter,computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print("The "+turn+" goes first")

        playing = True
        while playing:
            if turn == 'player':
                #Player Turn
                drawBoard(Board)
                move = Move(Board)
                makeMove(Board,playerLetter,move)
                if iswinner(Board,playerLetter):
                    drawBoard(Board)
                    print("Congrats!! You have won the game")
                    playing = False
                else:
                    if isfull(Board):
                        drawBoard(Board)
                        print("The game is tied")
                        break
                    else:
                        turn = 'computer'
            else:
                move = ComputerMove(Board,computerLetter)
                makeMove(Board,computerLetter,move)
                if iswinner(Board,computerLetter):
                    drawBoard(Board)
                    print("The computer has won. Better luck next time")
                    playing = False
                else:
                    if isfull(Board):
                        drawBoard(Board)
                        print("The game is tied")
                        break
                    else:
                        turn = 'player'
                
                

if __name__ == "__main__":
    main()
