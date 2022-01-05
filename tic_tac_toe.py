#board = list(input("Enter cells:"))
board = '         '
n = 3
#board = "XXXOO__O_" #X
#board = "XOXOXOXXO" #X
#board = "XOOOXOXXO" #O
#board = "XOXOOXXXO" #Draw
#board = "XO_OOX_X_" #Not Finished
#board = "XO_XO_XOX" #Imp
#board = "_O_X__X_X" #Imp
#oard = "_OOOO_X_X" #Imp
board = [[board[i * n + j ] for j in range(n)] for i in range(n)]
print("---------")
for i in range(n):
    print("|", *board[i], "|", sep=" ")
print("---------")
cells = [board[i][j] for i in range(n) for j in range(n)]
player = 'first'
while cells.count('X') + cells.count('O') < 9:
    while True:
        try:
            print("Enter the coordinates: ", end='')
            x, y = input().split()
        except EOFError:
            break
        
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("You should enter numbers!")
            continue
            
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        
        if board[x - 1][y - 1] in ['X', 'O']:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            if player == 'first':
                board[x - 1][y - 1] = 'X'
                player = 'second'
            else:
                board[x - 1][y - 1] = 'O'
                player = 'first'     
            print("---------")
            for i in range(n):
                print("|", *board[i], "|", sep=" ")
            print("---------")
            break
    lines = [list(board[i]) for i in range(n)] + [[board[i][j] for i in range(n)] for j in range(n)] + [[board[i][i] for i in range(n)]] + [[board[i][2 - i] for i in range(n)]]
    cells = [board[i][j] for i in range(n) for j in range(n)]
    if abs(cells.count('X') - cells.count('O')) > 1 or  ['X'] * n in lines and ['O'] * n in lines:
        print("Impossible")
    elif ['X'] * n not in lines and ['O'] * n not in lines and ' ' in cells:
        print("Game not finished")
        continue
    elif ['X'] * n not in lines and ['O'] * n not in lines and ' ' not in cells :
        print("Draw")
        break
    elif ['X'] * n in lines:
        print("X wins")
        break
    elif ['O'] * n in lines:
        print("O wins")
        break
    elif  ['X'] * n in lines and ['O'] * n in lines:
        print("Impossible")

        
    
    
    
