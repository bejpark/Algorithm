"""
#1260
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

#입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

#출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""

"""
#1
from collections import deque

def dfs(graph,start_node):
    print(start_node,end=' ')
    visited[start_node]=True
    for e in graph[start_node]:
        if not visited[e]:
            dfs(graph,e)

def bfs(graph,start_node):
    q=deque([start_node])
    while q:
        start_node=q.popleft()
        if not visited[start_node]:
            visited[start_node]=True
            print(start_node, end=' ')
            for e in graph[start_node]:
                if not visited[e]:
                    q.append(e)


                    
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for e in graph:
    e.sort()
visited=[False]*(n+1)
dfs(graph,v)
print()
visited=[False]*(n+1)
bfs(graph,v)
"""
#2 시간 더 소요

def bfs(graph,start_node):
    visited=[]
    need_visit=[start_node]
    while need_visit:
        visit=need_visit.pop(0)
        if visit not in visited:
            need_visit=need_visit + graph[visit]
            visited.append(visit)
        
    print(" ".join(map(str,visited)))

def dfs(graph,start_node):
    visited=[]
    need_visit=[start_node]
    while need_visit:
        visit=need_visit.pop(0)
        if visit not in visited:
            need_visit=graph[visit] + need_visit
            visited.append(visit)
        
    print(" ".join(map(str,visited)))

    
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for e in graph:
    e.sort()
dfs(graph,v)
bfs(graph,v)

