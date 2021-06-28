"""
#12100
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.

#출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
"""

#1 문제1: 배열의 softcopy, deepcopy.. 문제2: 초기 상태에 max넣어놓기
#하지만 코드가 좀 안이쁘다
import sys
sys.setrecursionlimit(50000)
n = int(input())
board = [list(map(int,input().split())) for i in range(n)]
val = max(map(max,board))
#print(board) 
def arrange(direction,B):
    Board = [item[:] for item in B]
    if direction ==0:#위
        for j in range(n):
            tmp = []
            for i in range(n):
                if Board[i][j]!=0:
                    tmp.append(Board[i][j])
            for i in range(len(tmp)):
                Board[i][j] = tmp[i]
            for i in range(len(tmp),n):
                Board[i][j] = 0
    elif direction ==1:#아래
        for j in range(n):
            tmp = []
            for i in range(n):
                if Board[i][j]!=0:
                    tmp.append(Board[i][j])
            for i in range(n-len(tmp)):
                Board[i][j] = 0
            for i in range(n-len(tmp),n):
                Board[i][j] = tmp[i-(n-len(tmp))]
    elif direction ==2:#<-
        for i in range(n):
            tmp = []
            for j in range(n):
                if Board[i][j]!=0:
                    tmp.append(Board[i][j])
            for j in range(len(tmp)):
                Board[i][j] = tmp[j]
            for j in range(len(tmp),n):
                Board[i][j] = 0        
    elif direction ==3:#->
        for i in range(n):
            tmp = []
            for j in range(n):
                if Board[i][j]!=0:
                    tmp.append(Board[i][j])
            for j in range(n-len(tmp)):
                Board[i][j] = 0
            for j in range(n-len(tmp),n):
                Board[i][j] = tmp[j-(n-len(tmp))]
    return Board


def update(direction,B):
    Board = arrange(direction,B)
    if direction == 0:
        for i in range(n):
            for j in range(1,n):
                if Board[j][i] !=0 and Board[j][i] == Board[j-1][i]:
                    Board[j-1][i] = Board[j-1][i]*2
                    Board[j][i] = 0
    elif direction ==1:
        for i in range(n):
            for j in range(n-2,-1,-1):
                if Board[j][i] !=0 and Board[j][i] == Board[j+1][i]:
                    Board[j+1][i] = Board[j+1][i]*2
                    Board[j][i] = 0
    elif direction ==2:
        for i in range(n):
            for j in range(1,n):
                if Board[i][j] !=0 and Board[i][j] == Board[i][j-1]:
                    Board[i][j-1] = Board[i][j-1]*2
                    Board[i][j] = 0
    elif direction ==3:
        for i in range(n):
            for j in range(n-2,-1,-1):
                if Board[i][j] !=0 and Board[i][j] == Board[i][j+1]:
                    Board[i][j+1] = Board[i][j+1]*2
                    Board[i][j] = 0
    result = arrange(direction,Board)
    return result

def dfs(B,count):
    global val
    BB = [item[:] for item in B]
    if count == 5:
        max_val = max(map(max,B))
        #print(max_val)
        if max_val > val:
            val = max_val
        #print(B)
    else:
        for i in range(4):
            #print('go')
            new = update(i,BB)
            if new != B:
                dfs(new,count+1)
                

dfs(board,0)
print(val)


"""
#2 4가지 방향을 90도 회전하는 배열을 만들면서 진행
from copy import deepcopy
N = int(input())
Board = [list(map(int,input().split())) for i in range(N)]


def rotate90(Board,N):
    NB = deepcopy(Board)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = Board[i][j]
    return NB

def convert(lst,N):
    new_list = [i for i in lst if i] #양수만 남긴다는 뜻
    for i in range(1,len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1]*=2
            new_list[i]=0
    new_list = [i for i in new_list if i]
    return new_list + [0]*(N-len(new_list))


def dfs(N,Board,count):
    ret = max([max(i) for i in Board])
    if count ==0:
        return ret
    for _ in range(4):
        X = [convert(i,N) for i in Board]
        if X != Board:
            ret = max(ret,dfs(N,X,count-1))

        Board = rotate90(Board,N)
    return ret
print(dfs(N,Board,5))
"""
