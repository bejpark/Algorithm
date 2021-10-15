#끔찍한문제다 정말
import sys
sys.setrecursionlimit(10 ** 5)

def choose_board(L): #회전시킬 부분테이블
    choose_size = 2**L
    for i in range(0,lenN,choose_size):
        for j in range(0,lenN,choose_size):
            rotate(i,j,choose_size) #부분테이블의 시작점과 크기를 보냄
    

def rotate(startX,startY,size): #해당 부분테이블 회전
    for i in range(size):
         for j in range(size):
            new_table[startX+j][startY+i]=table[startX+size-i-1][startY:startY+size][j]
            #"첫 세로줄의 값 = 마지막 가로줄 값" 으로 대응

def minus_board():
    count=0
    for i in range(lenN):
        for j in range(lenN):
            count=0
            for dx,dy in d:
                X=i+dx
                Y=j+dy
                if 0<=X<lenN and 0<=Y<lenN: #인접한 얼음이 있을 때 +1
                    if new_table[X][Y]>0:
                        count+=1
            if count<3 and new_table[i][j]>0: #3이 넘지않으면 칸 -1, 0인경우 음수가 됨 제외
                table[i][j]-=1

def search(x,y):
    global block_size

    visited[x][y]=True
    for dx,dy in d:
        X=x+dx
        Y=y+dy
        if 0<=X<lenN and 0<=Y<lenN:
            if table[X][Y]>0 and not visited[X][Y]:
                block_size+=1
                search(X,Y)
               

    
                

N,Q = map(int,input().split())
lenN = 2**N
table=[]
result_sum=0
block_size=0
max_size=0
d=[(0,1),(0,-1),(1,0),(-1,0)]
new_table=[[0 for _ in range(lenN)] for _ in range(lenN)]
visited=[[False for _ in range(lenN)] for _ in range(lenN)]


for i in range(lenN):
    table.append(list(map(int,input().split())))

orders=list(map(int,input().split()))


for i in orders:
    choose_board(i)
    table=[item[:] for item in new_table]
    minus_board()


for i in range(lenN):
        for j in range(lenN):
            result_sum+=table[i][j]#합 구하기
            if table[i][j] and not visited[i][j]:
                block_size=1
                search(i,j)
                max_size=max(max_size,block_size)


print(result_sum)
print(max_size)

