"""
#1495
Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다.
지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.

먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다.
이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다.
항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다.
즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다.
하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.

곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오.
모든 곡은 리스트에 적힌 순서대로 연주해야 한다.

#입력
첫째 줄에 N, S, M이 주어진다.
(1 ≤ N ≤ 100, 1 ≤ M ≤ 1000, 0 ≤ S ≤ M) 둘째 줄에는 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이가 주어진다.
이 값은 1보다 크거나 같고, M보다 작거나 같다.

#출력
첫째 줄에 가능한 마지막 곡의 볼륨 중 최댓값을 출력한다. 만약 마지막 곡을 연주할 수 없다면 (중간에 볼륨 조절을 할 수 없다면) -1을 출력한다.
"""
"""
#1 메모리 초과
n,s,m = map(int,input().split())
v=list(map(int,input().split()))
cal=[s]
cal2=[]
cannot=False
for i in range(n):
    while len(cal)!=0:
        x=cal.pop()
        a1=x+v[i]
        a2=x-v[i]
        if a1<=m:
            cal2.append(a1)
        if a2>=0:
            cal2.append(a2)
        
    if len(cal2)==0:
        cannot=True
    cal=cal2
    cal2=[]

    
if cannot==True:
    print(-1)
else:
    print(max(cal))
"""
#2 동적 프로그래밍 활용
n,s,m = map(int,input().split())
v=list(map(int,input().split()))
can=False

dp=[[0]*(m+1) for i in range(n+1)]
dp[0][s]=1

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j]==1:
            if j+v[i-1]<=m:
                dp[i][j+v[i-1]]=1
            if j-v[i-1]>=0:
                dp[i][j-v[i-1]]=1


for i in range(m,-1,-1):
    if dp[n][i]==1:
        print(i)
        can=True
        break

if can==False:
    print(-1)
    
