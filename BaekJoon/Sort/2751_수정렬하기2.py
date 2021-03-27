"""
#2751
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
#1
from sys import stdin
n=int(stdin.readline())
array=[]
for _ in range(n):
    array.append(int(stdin.readline()))

array.sort()
print("\n".join(map(str,array)))
"""
#2
rom sys import stdin

num = int(stdin.readline())
arr=[]
for _ in range(num):
    arr.append(int(stdin.readline()))

def merge(array):
    mid = len(array)//2
    j,k=0,0
    if len(array)!=1:
        array_left=merge(array[:mid])
        array_right=merge(array[mid:])
    else:
        return array
    for i in range(len(array)):
        if len(array_right)==k:
            array[i]=array_left[j]
            j+=1
        elif len(array_left)==j:
            array[i]=array_right[k]
            k+=1
        else:
            if array_left[j]>=array_right[k]:
                array[i]=array_right[k]
                k+=1
            else:
                array[i]=array_left[j]
                j+=1
    return array
print("\n".join(map(str,merge(arr))))
"""
