from collections import deque
from sys import stdin
def gravity():
    block_status=[0 for _ in range(n)]
    for j in range(n):
        for i in range(n-1):
            if board[i][j]==-1:
                continue
            if board[i+1][j]==-2:
                k = block_status[j]
                for x in range(0,k+1): #본인부터 위로 붙어있는 블록 수
                    board[i+1-x][j]=board[i-x][j]

                board[i - block_status[j]][j] = -2
            elif board[i+1][j]==-1: #검은 블록인 경우 block_status초기화
                block_status[j]=0
            elif board[i+1][j]>=0:
                block_status[j]+=1


def rotate(n):
    tmp_board=[b[:] for b in board]
    for i in range(n):
        for j in range(n):
            board[n-j-1][i] = tmp_board[i][j]

def bfs(i,j):
    cnt=0
    rainbowcnt=0
    visited[i][j] = True
    q=deque()
    visited_node=[(i,j)] #방문한 노드(이후 지울때 필요)
    q.append((i,j))
    while q:
        cnt += 1
        x,y = q.popleft()
        for dx,dy in d:
            X,Y=x+dx,y+dy
            if 0<=X<n and 0<=Y<n:
                if not visited[X][Y] and board[X][Y]!=-1: #방문 안했고 -1이 아닌 경우
                    if board[i][j]==board[X][Y] or board[X][Y]==0: #색이 같거나 무지개인 경우
                        if board[X][Y]==0:
                            rainbowcnt+=1
                        visited[X][Y]=True
                        visited_node.append((X,Y))
                        q.append((X,Y))

    for xx in range(n): #0은 다시 방문할 수 있음 False로 만들어서 다른 색에도 적용하게 해야한다.
        for yy in range(n):
            if board[xx][yy]==0:
                visited[xx][yy]=False
    return rainbowcnt, cnt, visited_node

n,m = map(int,stdin.readline().split())
board=[]
result=0
block_group_size=0
block_rainbow_size=0
block_group_idx=[0,0]
d=[(0,1),(0,-1),(1,0),(-1,0)]
visitnode=[]
visited=[[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,stdin.readline().split())))





while True:
    for i in range(n): #큰 그룹 찾기, 그 크기와 배열 저장
        for j in range(n):
            if board[i][j]>0 and not visited[i][j]: #색이 있는경우만 bfs
                rainbowsize, size,node=bfs(i,j)
                if block_group_size<size:
                    block_group_size=size
                    block_rainbow_size=rainbowsize
                    block_group_idx=[i,j]
                    visitnode=node
                elif block_group_size==size: #그룹 크기가 같을 때 무지개->행->렬 우선순위 따짐
                    if block_rainbow_size<=rainbowsize: #for 문이 행->렬순이기 때문에 무지개만 고려하고 최신으로 넣음
                        block_group_size = size
                        block_rainbow_size = rainbowsize
                        block_group_idx = [i, j]
                        visitnode = node
    if block_group_size<=1: #그룹이 없을 때 게임종료
        break

    for i,j in visitnode:
        board[i][j]=-2
    result+=block_group_size**2

    gravity()
    rotate(n)
    gravity()
    #1회 끝난 후 값을 초기화
    block_group_size = 0
    block_rainbow_size = 0
    block_group_idx = [0, 0]
    visitnode = []
    visited = [[False for _ in range(n)] for _ in range(n)]


print(result)

"""
5 3
2 2 -1 3 1
3 3 2 0 -1
0 0 0 1 2
-1 3 1 3 2
0 3 2 2 1
"""