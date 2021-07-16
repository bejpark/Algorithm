"""
#2014
K개의 소수가 있다. 이때, 이 소수들 중에서 몇 개를 곱해서 얻게 되는 수들이 있을 것이다. 
소수들을 선택할 때에는 같은 수를 선택해도 되며, 주어지는 소수 자체도 포함시키자.

예를 들어 세 소수가 2, 5, 7이었다면, 이러한 곱들을 오름차순으로 나타내 보면, 2, 4, 5, 7, 8, 10, 14, 16, 20, 25, 28, 32, 35, 등이 된다.

K개의 소수가 주어졌을 때, 이러한 소수의 곱들 중에서 N번째 수를 구해 보자. 단 정답은 231보다 작은 자연수이다.

#입력
첫째 줄에 K(1 ≤ K ≤ 100), N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 K개의 소수가 오름차순으로 주어진다. 
같은 소수가 여러 번 주어지는 경우는 없으며, 주어지는 소수는 모두 541보다 작거나 같은 자연수이다.

#출력
첫째 줄에 문제에서 설명한 대로 소수의 곱을 나열했을 때, N번째 오는 것을 출력한다.
"""
"""
#1 Fail
import heapq
k,n = map(int,input().split())
prime = list(map(int,input().split()))
arr = []
for i in range(k):
    heapq.heappush(arr,prime[i])
for i in range(k):
    for j in range(len(arr)):
        val = prime[i]*arr[j]
        if val not in arr:
            heapq.heappush(arr,val)
for _ in range(n):
    result = heapq.heappop(arr)
    print(result)
print(result)
"""
#2 최소값을 pop하여 그것과 다시 곱한것들을 push 해주면 순서 상 문제가 없음, 효율적
import heapq
k,n = map(int,input().split())
prime = list(map(int,input().split()))
lst,ck = prime[:], set()

heapq.heapify(lst)
count = 0
while count<n:
    val = heapq.heappop(lst)
    if val in ck: #중복이면 넘어감
        continue
    count+=1
    ck.add(val)
    for i in prime:
        heapq.heappush(lst,i*val)
print(val)
