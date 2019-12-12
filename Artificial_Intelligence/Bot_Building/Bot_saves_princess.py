def displayPathtoPrincess(n,grid):
  #print all the moves here
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                pr,pc = i,j
            if grid[i][j]=="m":
                r,c = i,j
    while (pr,pc)!=(r,c):
        diff = [pr-r,pc-c]
        if diff[0]>0: 
            print("DOWN")
            r+=1
        elif diff[0]<0: 
            print("UP")
            r-=1
        elif diff[1]>0: 
            print("RIGHT")
            c+=1
        elif diff[1]<0: 
            print("LEFT")
            c-=1
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)