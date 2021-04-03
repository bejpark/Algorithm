"""
#1927
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

#입력
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
입력되는 자연수는 231보다 작다.

#출력
입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
"""
"""
#1
import heapq
import sys
n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    if num==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)        
"""
#2
import sys
heap=[0]
def heappush(arr,data):
    i = len(arr)
    
    arr.append(0)
    if len(arr)==1:
        arr[i]=data
    else:
        while i!=1 and data<arr[i//2]:
            arr[i]=arr[i//2]
            i=i//2
        arr[i]=data

def heappop(arr):
    print(arr[1])
    arr[1]=arr[-1]
    data=arr[1]
    i=1
    del arr[-1]
    while i*2<=len(arr)-1: #자식노드 있는 경우
        if i*2==len(arr)-1: #우측 자식노드 없을 때
            if arr[i*2]<data:
                arr[i]=arr[i*2]
                arr[i*2]=data
                i=i*2
            else:
                break
        elif arr[i*2]<arr[i*2+1] and arr[i*2]<data:
            arr[i]=arr[i*2]
            arr[i*2]=data
            i=i*2
        elif arr[i*2]>=arr[i*2+1] and arr[i*2+1]<data:
            arr[i]=arr[i*2+1]
            arr[i*2+1]=data
            i=i*2+1
        else:
            arr[i]=data
            break
            
n=int(sys.stdin.readline())
for _ in range(n):
    num=int(sys.stdin.readline())
    if num==0:
        if len(heap)==1:
            print(0)
        else:
            heappop(heap)
    else:
        heappush(heap,num)   
    
