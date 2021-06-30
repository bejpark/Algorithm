"""
#1932
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

#입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

#출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
"""
"""
#1 일반적인 재귀로는 상당한 시간초과
import sys
n = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[]
for i in range(n):
    dp.append([0 for i in range(i+1)])
dp[0][0] = arr[0][0]
#print(arr)
def search(depth,ans,idx):
    dp[depth-1][idx] = max(ans,dp[depth-1][idx])
    if depth == n:
        return
    search(depth+1,ans+arr[depth][idx],idx)
    search(depth+1,ans+arr[depth][idx+1],idx+1)
search(1,dp[0][0],0)
print(max(dp[-1]))
"""
#2 중간값들은 이전의 최댓값을 받아와 계산함으로 연산 수를 줄인다.
import sys
n = int(sys.stdin.readline())
mat = []
dp = []
#[[0 for _ in range(n+1) for i in range(n+1)]]
for i in range(1,n+1):
    mat.append(list(map(int,sys.stdin.readline().split())))
    dp.append([0 for _ in range(i)])
dp[0] =mat[0]
dp[1][0] = dp[0][0]+mat[1][0]
dp[1][1] = dp[0][0]+mat[1][1]
for i in range(2,n):
    dp[i][0] = mat[i][0]+dp[i-1][0] #양 끝점은 만들어준다
    dp[i][-1] = mat[i][-1]+dp[i-1][-1]
    for j in range(1,i):
        dp[i][j] = mat[i][j]+max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[-1]))

