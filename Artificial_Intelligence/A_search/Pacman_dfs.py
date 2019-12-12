pacman = list(map(int,input().split()))
food = list(map(int,input().split()))
board_size = list(map(int,input().split()))
board = [input() for _ in range(board_size[0])]
vis = [[0 for _ in range(board_size[1])] for _ in range(board_size[0])]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
road = [[pacman[0],pacman[1]]]
ans = []
def dfs(r,c,road):
    global ans
    if board[r][c]==".":
        if not ans or len(ans)>len(road):
            ans = road
        vis[r][c]=0
        return
    for i in range(4):
        if board[r+dx[i]][c+dy[i]]!="%" and vis[r+dx[i]][c+dy[i]]!=1:
            vis[r+dx[i]][c+dy[i]]=1
            dfs(r+dx[i],c+dy[i],road + [[r+dx[i],c+dy[i]]])
    vis[r][c]=0
    return
dfs(pacman[0],pacman[1],road)
print(len(ans))
for a in ans:
    print(a[0],a[1])
