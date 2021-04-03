"""
#1766
민오는 1번부터 N번까지 총 N개의 문제로 되어 있는 문제집을 풀려고 한다. 문제는 난이도 순서로 출제되어 있다. 즉 1번 문제가 가장 쉬운 문제이고 N번 문제가 가장 어려운 문제가 된다.

어떤 문제부터 풀까 고민하면서 문제를 훑어보던 민오는, 몇몇 문제들 사이에는 '먼저 푸는 것이 좋은 문제'가 있다는 것을 알게 되었다.
예를 들어 1번 문제를 풀고 나면 4번 문제가 쉽게 풀린다거나 하는 식이다.
민오는 다음의 세 가지 조건에 따라 문제를 풀 순서를 정하기로 하였다.

N개의 문제는 모두 풀어야 한다.
먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
가능하면 쉬운 문제부터 풀어야 한다.
예를 들어서 네 개의 문제가 있다고 하자.
4번 문제는 2번 문제보다 먼저 푸는 것이 좋고, 3번 문제는 1번 문제보다 먼저 푸는 것이 좋다고 하자.
만일 4-3-2-1의 순서로 문제를 풀게 되면 조건 1과 조건 2를 만족한다.
하지만 조건 3을 만족하지 않는다. 4보다 3을 충분히 먼저 풀 수 있기 때문이다.
따라서 조건 3을 만족하는 문제를 풀 순서는 3-1-4-2가 된다.

문제의 개수와 먼저 푸는 것이 좋은 문제에 대한 정보가 주어졌을 때, 주어진 조건을 만족하면서 민오가 풀 문제의 순서를 결정해 주는 프로그램을 작성하시오.

#입력
첫째 줄에 문제의 수 N(1 ≤ N ≤ 32,000)과 먼저 푸는 것이 좋은 문제에 대한 정보의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다.
이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.

항상 문제를 모두 풀 수 있는 경우만 입력으로 주어진다.

#출력
첫째 줄에 문제 번호를 나타내는 1 이상 N 이하의 정수들을 민오가 풀어야 하는 순서대로 빈칸을 사이에 두고 출력한다.

"""
"""
반례가 많고 문제가 모호하다.
5 1
5 1 인 경우
1) 23451
2) 51234
중 어느것인지 판단이 어렵다. 결론은 1)이 맞음

5 2
1 4
5 2 인 경우
13524가 아닌
13452가 되어야한다.

#1 - 실패
import heapq
N,M=map(int,input().split())
heap=[]
waiting_list=[]
first_list=[]
result_list=[]

for _ in range(M):
    A,B=map(int,input().split())
    heapq.heappush(heap,(B,A))
print(heap)
for i in range(1,N+1):
    print("case",i)
    if len(heap)!=0 and i==heap[0][0]:
        waiting_list.append(i)
        first_list.append(heapq.heappop(heap)[1])
        print(first_list,"first list added")
        print(waiting_list,"waiting list added")
    else:
        result_list.append(i)
        print(result_list,"result list added")
    if len(first_list)!=0 and first_list[0]==i:
        print("get in last if, pop and append result")
        first_list.pop(0)
        result_list.append(waiting_list.pop(0))
        print("append waiting list, and result list is",result_list)
        if i==N:
            while len(first_list)!=0:
                first_list.pop(0)
                result_list.append(waiting_list.pop(0))

        
print(' '.join(map(str,result_list)))
"""
#2 위상 정렬.. 원리 기억하기 간선 제거하는 방식
import heapq

N,M=map(int,input().split())
array=[[] for i in range(N+1)]
indegree=[0]*(N+1)
heap=[]
result=[]

for _ in range(M):
    x,y = map(int,input().split())
    array[x].append(y)
    indegree[y]+=1

for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)
while heap:
    data=heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y]-=1
        if indegree[y]==0:
            heapq.heappush(heap,y)

for i in result:
    print(i,end=' ')






