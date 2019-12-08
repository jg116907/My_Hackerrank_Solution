# Head ends here
from collections import defaultdict

def next_move(posr, posc, board):
    trash = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "d":
                if (i,j)==(posr,posc):
                    print("CLEAN")
                    return
                else:
                    trash.append((i,j))
    mindis = len(board)*2+1 
    target = ()
    for t in trash:
        dis = abs(t[0] - posr) + abs(t[1] - posc)
        if mindis>dis:
            mindis = dis
            target = t
    if target[0] - posr < 0: print("UP")
    elif target[0] - posr > 0: print("DOWN")
    elif target[1] - posc < 0: print("LEFT")
    elif target[1] - posc > 0: print("RIGHT")
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)