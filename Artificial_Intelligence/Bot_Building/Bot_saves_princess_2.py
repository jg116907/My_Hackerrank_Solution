def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                pr,pc = i,j
    diff = [pr-r,pc-c]
    if diff[0]>0: return "DOWN"
    elif diff[0]<0: return "UP"
    elif diff[1]>0: return "RIGHT"
    elif diff[1]<0: return "LEFT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))