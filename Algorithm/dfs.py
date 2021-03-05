graph = dict()

graph['A']=['B','C'] #그래프에서 인접한 점들
graph['B']=['A','D']
graph['C']=['A','G','H','I']
graph['D']=['B','E','F']
graph['E']=['D']
graph['F']=['D']
graph['G']=['C']
graph['H']=['C']
graph['I']=['C','J']
graph['J']=['I']


def dfs(graph, start_node): #bfs와 거의 동일함 need_visit이 queue와 stack의 차이만 있음
    visited = list()
    need_visit = list()
    count = 0

    need_visit.append(start_node)
    while need_visit:
        count+=1
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

print(dfs(graph,'A'))
