"""
#1697
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

#입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

#출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""
"""
#1 시간초과
import time
from collections import deque
x,k=map(int,input().split())
start=time.time()

def bfs():
    v=x
    visited=[]
    need_visit=deque()
    need_visit.append(v)
    while v!=k:
        v=need_visit.popleft()
        need_visit.append(v+1)
        need_visit.append(v-1)
        need_visit.append(v*2)
        if v not in visited:
            visited.append(v)
    return len(visited)

result=bfs()
count=0
while result!=1:
    result=result//2
    count+=1
print(count)
end=time.time()
print(end-start)
"""


#2
from collections import deque


x,k=map(int,input().split())
MAX=100001
arr=[0]*MAX
def bfs():
    v=x
    need_visit=deque()
    need_visit.append(v)
    while v!=k:
        v=need_visit.popleft()
        for vv in (v-1,v+1,v*2):
            if 0<=vv<MAX and not arr[vv]:
                arr[vv]=arr[v]+1
                need_visit.append(vv)
    return arr[v]

print(bfs())



