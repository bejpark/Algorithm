"""
#17269
시윤이는 좋아하는 이성이 생기면 가장 먼저 이름궁합부터 본다.
이름궁합을 보는 방법은 간단하다. 먼저 이름을 알파벳 대문자로 적는다. 각 알파벳 대문자에는 다음과 같이 알파벳을 적는데 필요한 획수가 주어진다.
예를 들어, 두 사람의 이름인 LEESIYUN, MIYAWAKISAKURA 를 같이 표현했을 때 다음과 같이 먼저 주어진 이름부터 한 글자씩 적는다.

두 사람의 이름을 알파벳 대문자로 표현한 뒤, 한 글자씩 번갈아가며 적는다.

예시 :  L M E I E Y S A I W Y A U K N I S A K U R A

예시처럼 이름이 남을 경우엔 뒤에 남은 글자인 S A K U R A를 맨 뒤에 적는다.
그러고 나서 알파벳을 대응하는 숫자로 바꾸고 각 숫자와 그 숫자의 오른쪽 숫자와 더한 것을 밑에 적는다. 더한 숫자가 10이 넘을 경우엔 일의 자리 수만 남긴다. 이 과정을 반복하여 숫자가 2개만 남았을 때 남은 숫자가 두 사람의 궁합이 좋을 확률이 된다.

과정을 자세히 나타내면 다음과 같다.

초기 상태 : 1 3 4 1 4 2 1 3 1 1 2 3 1 3 2 1 1 3 3 1 2 3
한번 수행 :  4 7 5 5 6 3 4 4 2 3 5 4 4 5 3 2 4 6 4 3 5
두번 수행 :   1 2 0 1 9 7 8 6 5 8 9 8 9 8 5 6 0 0 7 8
세번 수행 :    3 2 1 0 6 5 4 1 3 7 7 7 7 3 1 6 0 7 5
...
19번 수행 :                  5 7 0
20번 수행 :                   2 7
따라서 LEESIYUN와 MIYAWAKISAKURA이 궁합이 좋을 확률이 27%이다.

#입력
첫 번째 줄에 이름의 길이 N과 M을 받는다. (2 ≤ N, M ≤ 100)

다음 줄에 이름 A와 B를 입력받는다. 이름은 반드시 알파벳 대문자만 주어진다.

#출력
A와 B의 이름궁합이 좋을 확률을 %로 출력한다. 단, 십의 자리가 0일 경우엔 일의 자리만 출력한다.
"""
n,m = map(int,input().split())
a,b = input().split()
num_1= 'CGIJLOSUVWZ'
num_2= 'BDNPQRTXY'
num_3= 'AFHKM'
num_4= 'E'
x = max(n,m)
array=[]
for i in range(x):
    if i < n:
        if a[i] in num_1:
            array.append(1)
        elif a[i] in num_2:
            array.append(2)
        elif a[i] in num_3:
            array.append(3)
        elif a[i] in num_4:
            array.append(4)
    if i < m:
        if b[i] in num_1:
            array.append(1)
        elif b[i] in num_2:
            array.append(2)
        elif b[i] in num_3:
            array.append(3)
        elif b[i] in num_4:
            array.append(4)
            
for i in range(n+m-2):
    for j in range(n+m-i-1):
        array[j] = array[j]+array[j+1]
        """
        if val>=10:
            array[j]= val-10
        else:
            array[j] = val
        """
    #array.pop()
"""
if array[0]==0:
    print(str(array[1])+'%')
else:
    print(''.join(map(str,array))+'%')
"""

print("{}%".format(array[0]%10*10+array[1]%10))
