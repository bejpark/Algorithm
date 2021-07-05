"""
#1915
n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

0	1	0	0
0	1	1	1
1	1	1	0
0	0	1	0
위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다. 

#입력
첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

#출력
첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

"""
# deepcopy 사용하면 시간이 좀 더 걸림.. item[:] for item in arr 사용하면 조금더 빠름
n,m = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
dp = [item[:] for item in arr] #1차원의 경우는 dp=arr[:]
for i in range(1,n):
    for j in range(1,m):
        if dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1] and dp[i][j]:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1

val=0
for k in range(n):
    val = max(val,max(dp[k]))
print(val*val)
"""
n,m = map(int,input().split())
arr = [[0 for _ in range(m+1)] for i in range(n+1)]
dp = [[0 for _ in range(m+1)] for i in range(n+1)]
for i in range(n):
    for idx,j in enumerate(list(map(int,list(input())))):
        arr[i+1][idx+1] = j
mx=0

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j]:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            mx = max(dp[i][j],mx)
print(mx**2)
"""