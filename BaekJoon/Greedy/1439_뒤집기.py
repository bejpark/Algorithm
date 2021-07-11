"""
#1439
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다.
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

1. 전체를 뒤집으면 1110011이 된다.
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.

하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.

#입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다.

#출력
첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.
"""
"""
#1
card=input()
before=int(card[0])
if before==1:
    ones=1
    zeros=0
elif before==0:
    ones=0
    zeros=1
for i in card:
    if i=='0' and before==1:
        zeros+=1
        before=0
    elif i=='1' and before==0:
        ones+=1
        before=1
print(min(ones,zeros))

#before 대신
#for i in range(len(data)) 로 접근하여 data[i]와 data[i+1]을 비교해도됨
"""
"""
#2
card = input()
prev = card[0]
if prev=='1':
    one=1
    zero=0
else:
    one=0
    zero=1

for i in card:
    if i!=prev:
        if i=='1':
            one+=1
        else:
            zero+=1
        prev = i
print(min(zero,one))
"""
#3 바뀌는 수를 조사한 후 계산
card, result = input(),0
for i in range(1,len(card)):
    if card[i]!=card[i-1]:
        result+=1
print((result+1)//2)
