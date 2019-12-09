def nextMove(posr, posc, board):
    target = ()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "d":
                if (i,j)==(posr,posc):
                    print("CLEAN")
                    return
                else:
                    target = (i,j)
    if target[0] - posr < 0: print("UP")
    elif target[0] - posr > 0: print("DOWN")
    elif target[1] - posc < 0: print("LEFT")
    elif target[1] - posc > 0: print("RIGHT")
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)