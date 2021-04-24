"""
#1325
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 
이 회사는 N개의 컴퓨터로 이루어져 있다. 
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

#입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

#출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
"""
#메모리초과..시간초과.. 해결은했지만 시간이 매우 높다
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range (n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[y].append(x)

def bfs(graph,start):
    step=0
    need_visit=deque([start])
    visited=[False]*(n+1)
    visited[start]=True
    while need_visit:
        node=need_visit.popleft()
        for e in graph[node]:
            if not visited[e]:
                need_visit.append(e)
                visited[e]=True
                step+=1
    return step
max=0
result=[]
for i in range(1,n+1):
    length=bfs(graph,i)
    if max<length:
        max=length
        result=[i]
    elif max==length:
        max=length
        result.append(i)
for e in result:
    print(e,end=" ")
