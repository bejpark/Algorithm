"""
#1427
배열을 정렬하는 것은 쉽다.
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

#입력
첫째 줄에 정렬하고자하는 수 N이 주어진다.
N은 1,000,000,000보다 작거나 같은 자연수이다.

#출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""
"""
#1
arr=input()
arr=list(arr)
arr.sort(reverse=True)
print("".join(arr))
"""

#2
arr=input()
arr=list(map(int,arr))
result=[]
while(len(arr)!=0):
    max_val=0
    for i in arr:
        if(max_val<i):
            max_val=i
    result.append(max_val)
    arr.pop(arr.index(max_val))
print("".join(map(str,result)))

"""
#3
arr=input()
for i in range(9,-1,-1):
    for j in arr:
        if int(j)==i:
            print(i,end='')
"""
