"""
#11055
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

#입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

#출력
첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.
"""
"""
#1 틀렸다 햇갈린다 역시 5,1,2,3,100 인경우 반례
n = int(input())

arr = list(map(int,input().split()))
dp = [(arr[0],arr[0])]
key = arr[0]
for i in range(1,n):
    result, last_val = dp[-1]
    if arr[i]>last_val:
        result = result+arr[i]
        dp.append((result, arr[i]))
        key = max(key,result)
    else:
        for res,last in dp[::-1]:
            if last < arr[i]:
                dp.append((res+arr[i],arr[i]))
                key = max(key,res+arr[i])
                break
print(key)
#print(dp)
"""
#2 바로앞값이 아니라 처음부터 갱신시켜도 시간이 얼마안듬 .. 이건몰랐지 
import copy
n,arr = int(input()), list(map(int,input().split()))
dp = copy.deepcopy(arr)

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(arr[i]+dp[j],dp[i])
print(max(dp))

"""
#만약 해당 수열을 출력한느 문제라면
import copy
n,arr = int(input()), list(map(int,input().split()))
dp = copy.deepcopy(arr)
rev = [i for i in range(n)]
idx =0

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j] and dp[i] < arr[i]+dp[j]:
            dp[i] = arr[i]+dp[j]
            rev[i] = j
    if dp[idx]<dp[i]:
        idx=i
    
print(dp[idx])
while rev[idx]!=idx:
    print(arr[idx],sep=" ")
    idx=rev[idx]
print(arr[idx])
"""
