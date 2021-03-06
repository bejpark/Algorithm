"""
#16768
With plenty of free time on their hands (or rather, hooves), the cows on Farmer John's farm often pass the time by playing video games.
One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.

The game of Mooyo Mooyo is played on a tall narrow grid N cells tall (1≤N≤100) and 10 cells wide. Here is an example with N=6:
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223

Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). 
Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.

Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, and they have the same nonzero color.
Any time a connected region exists with at least K cells, its haybales all disappear, turning into zeros. 
If multiple such connected regions exist at the same time, they all disappear simultaneously. Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros.
In the resulting configuration, there may again be connected regions of size at least K cells.
If so, they also disappear (simultaneously, if there are multiple such regions), then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least K exist.

Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.

#입력
The first line of input contains N and K (1≤K≤10N). 
The remaining N lines specify the initial state of the board.

#출력
Please output N lines, describing a picture of the final board state.
"""
"""
#1 2차원 배열 인덱싱 ...
import sys
sys.setrecursionlimit(10000)
N, K = map(int,input().split())
board = [list(map(int,input())) for i in range(N)]
visited = [[False]*10 for i in range(N)]
delete = [[False]*10 for i in range(N)]

val = 0
d = [(0,1),(0,-1),(1,0),(-1,0)]
count = 0
def dfs(x,y,key):
    global count
    visited[x][y] = True
    delete[x][y]=True
    for dx, dy in d:
        X = x+dx
        Y = y+dy
        if X<0 or X>=N or Y<0 or Y>=10:
            continue
        if board[X][Y] == key and not visited[X][Y]:
            dfs(X,Y,key)
            count+=1

def update():
    for i in range(N):
        for j in range(10):
            if board[i][j] == 'X':
                if i>=1:
                    board[1:i+1][j] = board[:i][j]
                    board[0][j] = 0
                else:
                    board[i][j] = 0

while True:              
    mooyo = 0
    for i in range(N):
        for j in range(10):
            if board[i][j] !=0 and not visited[i][j]:
                val = board[i][j]
                dfs(i,j,val)
                for ii in range(N):
                    for jj in range(10):
                        if delete[ii][jj]:
                            if count >=K:
                                board[ii][jj] = 'X'
                                mooyo = 1
                            delete[ii][jj] = False
                count = 0
    if mooyo == 0 :
        break
    else:
        update()
for i in range(N):
    print(delete[i])
for i in range(N):
    print(board[i])
"""
import sys
sys.setrecursionlimit(10000)
def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N,K = map(int,input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)
dx, dy = [0,1,0,-1], [1,0,-1,0]


def dfs(x,y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx,yy = x+dx[i],y+dy[i]
        if xx<0 or xx>=N or yy<0 or yy>=10:
            continue
        if ck[xx][yy] or M[x][y]!= M[xx][yy]: #방문했거나 다른 수
            continue
        ret += dfs(xx,yy)
    return ret

def dfs2(x,y,val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx,yy = x+dx[i],y+dy[i]
        if xx<0 or xx>=N or yy<0 or yy>=10:
            continue
        if ck2[xx][yy] or M[xx][yy]!=val: #방문했거나 다른 수
            continue
        dfs2(xx,yy,val)

def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] !='0':
                tmp.append(M[j][i])
        for j in range(N-len(tmp)):
            M[j][i] = '0'
        for j in range(N-len(tmp),N):
            M[j][i] = tmp[j-(N-len(tmp))]




while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j]=='0' or ck[i][j]:
                continue
            res = dfs(i,j) #개수세기
            if res >=K:
                dfs2(i,j,M[i][j]) #지우기
                exist = True
    
    if not exist:
        break
    down() #정리


for i in M:
    print(''.join(i))