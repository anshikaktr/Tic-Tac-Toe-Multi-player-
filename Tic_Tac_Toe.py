import random

X_marks=[0,0,0,0,0,0,0,0,0]
Z_marks=[0,0,0,0,0,0,0,0,0]
gameplay= True
def printboard():
    # print(f' 0 | 1 | 2 ')
    # print(f'---|---|---')
    # print(f' 3 | 4 | 5 ')
    # print(f'---|---|---')
    # print(f' 6 | 7 | 8 ')

    Num = lambda a: 'X' if X_marks[a] else ('O' if Z_marks[a] else a )

    print(f' {Num(0)} | {Num(1)} | {Num(2)} ')
    print(f'---|---|---')
    print(f' {Num(3)} | {Num(4)} | {Num(5)} ')
    print(f'---|---|---')
    print(f' {Num(6)} | {Num(7)} | {Num(8)} ')

def CheckPlace(to_check):
    global gameplay
    if to_check == 1:
        print('Place pre-occupied\nGame Over.')
        gameplay=False

def CheckWin(Check_for,xo):
    global gameplay
    win_sequence=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in win_sequence:
        if Check_for[win[0]]==Check_for[win[1]]==Check_for[win[2]]==1:
            print(xo,"WON")
            printboard()
            gameplay=False

def CheckTie():
    global gameplay
    Board = X_marks + Z_marks
    ones = 0
    # print(Board)
    if Board.count(1)==9:
        print("Match Drawn")
        printboard()
        gameplay=False

def play():
    print("X goes First\n")
    turn=1         #1 for X and 0 for O
    global gameplay
    while gameplay:
        printboard()
        if turn==1:
            print("X's turn")
            pos = int(input("Enter the position "))
            CheckPlace(X_marks[pos])        # Already in the spot
            CheckPlace(Z_marks[pos])        # Already in the spot
            X_marks[pos] = 1
        
        else:
            print("O's turn")
            pos = int(input("Enter the position "))
            CheckPlace(X_marks[pos])        # Already in the spot
            CheckPlace(Z_marks[pos])        # Already in the spot
            Z_marks[pos] = 1
    #check for winner
        CheckWin(X_marks,"X")
        CheckWin(Z_marks,"O")
    #check for tie
        CheckTie()

        turn= 1-turn

try:
    print("Let's play Tic-Tac-Toe\n ")
    play()

except Exception as e:
    print(e)