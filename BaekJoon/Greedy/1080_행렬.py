"""
#1080
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 
이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 -> 1, 1 -> 0)

#입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

#출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
"""
#왜 이렇게하면 정답인지 잘 모르겠다 ..
def flip(x,y):
    for i in range(3):
        for j in range(3):
            arr1[x+i][y+j]^=1

n,m = map(int,input().split())
arr1 = [list(map(int,input())) for _ in range(n)]
arr2 = [list(map(int,input())) for _ in range(n)]
gap = [[0]*m for _ in range(n)]
ans=0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]:
            flip(i,j)
            ans+=1

if arr1!=arr2:
    print(-1)
else:
    print(ans)
