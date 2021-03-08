myedges = [
    (7,'A','B'), (5,'A','D'),
    (8,'B','C'),(9,'B','D'),(7,'B','E'),
    (5,'C','E'),
    (7,'D','E'),(6,'D','F'),
    (8,'E','F'),(9,'E','G'),
    (11,'F','G')
]

from collections import defaultdict
from heapq import *

def prim(start_node,edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight,n1,n2))
        adjacent_edges[n2].append((weight,n1,n2))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list) #heapify를 통해 최소 힙으로 정렬

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes: #인접하다면 연결한다.
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))

            for edge in adjacent_edges[n2]: #연결된 노드의 인접한 선들 추가
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list,edge)
                
    return mst
        

print(prim('A',myedges))
