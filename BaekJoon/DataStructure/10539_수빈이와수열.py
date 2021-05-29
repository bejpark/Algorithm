"""
#10539
수빈이는 심심해서 수열을 가지고 놀고 있다. 먼저, 정수 수열 A를 쓴다.
그리고 그 아래에 정수 수열 A의 해당 항까지의 평균값을 그 항으로 하는 정수 수열 B를 쓴다. 

예를 들어, 수열 A가 1, 3, 2, 6, 8이라면, 수열 B는 1/1, (1+3)/2, (1+3+2)/3, (1+3+2+6)/4, (1+3+2+6+8)/5, 즉, 1, 2, 2, 3, 4가 된다. 

수열 B가 주어질 때, 수빈이의 규칙에 따른 수열 A는 뭘까?

#입력
첫째 줄에는 수열 B의 길이만큼 정수 N(1 ≤ N ≤ 100)이 주어지고, 둘째 줄에는 수열 Bi를 이루는 N개의 정수가 주어진다. (1 ≤ Bi ≤ 109)

#출력
첫째 줄에는 수열 A를 이루는 N개의 정수를 출력한다. (1 ≤ Ai ≤ 109)
"""
"""
n = int(input())
array = list(map(int,input().split()))
new_array = [0]*n
data = 0
for i in range(n):
    new_array[i] = (i+1) * array[i] - data
    data = data + new_array[i]
print(' '.join(map(str,new_array)))
"""

#2
n, a = int(input()), list(map(int,input().split()))
b = [a[0]]
for i in range(1,n):
    b.append(a[i]*(i+1) - sum(b))
print(b)
    
