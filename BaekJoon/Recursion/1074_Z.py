"""
#1074
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

#입력
첫째 줄에 정수 N, r, c가 주어진다.

#출력
r행 c열을 몇 번째로 방문했는지 출력한다.

#제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N
"""

"""
#1 시간초과,메모리초과
n,r,c=map(int,input().split())

matrix=[[0 for col in range(2**n)] for row in range(2**n)]

#Z(시작x,시작y,사이즈,가장큰수+1)

def Z(start_row,start_col,size,max_node):
    start_node=max_node-(size**2)
    if size==1: #가장 작은단위일때 그자리에 값 저장
        matrix[int(start_row)][int(start_col)]=max_node-1
    else:
        if r<start_row+size/2 and c<start_col+size/2:
            Z(start_row,start_col,size/2,start_node+(max_node-start_node)/4)
        if r<start_row+size/2 and c>=start_col+size/2:
            Z(start_row,start_col+size/2,size/2,start_node+(max_node-start_node)/4*2)
        if r>=start_row+size/2 and c<start_col+size/2:
            Z(start_row+size/2,start_col,size/2,start_node+(max_node-start_node)/4*3)
        if r>=start_row+size/2 and c>=start_col+size/2:
            Z(start_row+size/2,start_col+size/2,size/2,start_node+(max_node-start_node))
  

Z(0,0,2**n,int((2**n)**2))
print(int(matrix[r][c]))

#2 시간초과
def solve(n,x,y):
    global result
    if n==2:
        if x==r and y==c:
            print(result)
            return
        result+=1
        if x==r and y+1==c:
            print(result)
            return
        result+=1
        if x+1==r and y==c:
            print(result)
            return
        result+=1
        if x+1==r and y+1==c:
            print(result)
            return
        result+=1
        return
    solve(n/2,x,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n/2,y)
    solve(n/2,x+n/2,y+n/2)
result=0
n,r,c=map(int,input().split())
solve(2**n,0,0)

"""
"""
#3 해결 : 재귀 접근 자체를 구하고자 하는 좌표영역 안에서만 실행하도록 조건문 추가
import sys
n,r,c=map(int,sys.stdin.readline().split())


#Z(시작x,시작y,사이즈,마지막 수+1)

def Z(row,col,size,val):
    first_val=val-(size**2) #해당 사분면의 처음과 마지막 값 구해서 인덱스 계산
    if size==1: #가장 작은단위일때 그자리에 값 저장
        if row==r and col==c:
            print(int(val-1))
    else:
        G = (val-first_val)/4 #처음값과 마지막값+1의 차이를 4로 나누면 사분면 영역 분할 가능
        if r<row+size/2 and c<col+size/2:
            Z(row,col,size/2,first_val+G)
        elif r<row+size/2 and c>=col+size/2:
            Z(row,col+size/2,size/2,first_val+G*2)
        elif r>=row+size/2 and c<col+size/2:
            Z(row+size/2,col,size/2,first_val+G*3)
        else:
            Z(row+size/2,col+size/2,size/2,first_val+G*4)
  

Z(0,0,2**n,int((2**n)**2))
"""

"""

#4 06.09 재시도
import sys
n,r,c=map(int,sys.stdin.readline().split())

length = 2**n

def Z(start_value, length, x,y):
    cut = length/2
    value = cut**2 #사분면의 한 덩어리 크기

    #print('start : ',start_value)
    #print('cut : ',cut)
    #print('value : ',value)
    if length == 1:
        print(int(start_value))
    else:
        if x >= cut and y >= cut: #3
            Z(start_value + value*3, cut, x-cut, y-cut)
        elif x < cut and y >= cut: #2
            Z(start_value + value*2, cut, x, y-cut)
        elif x >= cut and y < cut: #1
            Z(start_value + value, cut, x-cut, y)
        elif x < cut and y < cut: #0
            Z(start_value, cut, x, y)

Z(0,length,c,r)

"""

#5 간단한 코드
N,r,c = map(int,input().split())
def Z(size,x,y):
    if size==1:
        return 0
    size//=2
    for i in range(2):
        for j in range(2):
            if x<size*(i+1) and y<size*(j+1):
                return (i*2+j)*size*size + Z(size,x-size*i,y-size*j)
print(Z(2**N,r,c))












