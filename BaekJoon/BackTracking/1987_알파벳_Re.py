"""
#1987
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

#입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다.
(1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

#출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
"""
"""
#1 오답, DFS가 아닌 BFS사용해야함
r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(input())

result = []

def test(array,x,y,step):
    global result
    if (0<=x and x<r and 0<=y and y<c):
        if board[x][y] not in array:
            array.append(board[x][y])
            test(array,x+1,y,step+1)
            test(array,x,y+1,step+1)
            test(array,x-1,y,step+1)
            test(array,x,y-1,step+1)
            print(step)
            result.append(step)
test([],0,0,1)
print(max(result))
"""
#2
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    global result
    q=set()
    q.add((x,y,board[x][y]))
    while q:
        x,y,step = q.pop()
        result=max(result,len(step))
        print(result)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx and nx<r and 0<=ny and ny<c and board[nx][ny] not in step):
                q.add((nx,ny,step+board[nx][ny]))
r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(input())
result = 0
bfs(0,0)
print(result)

