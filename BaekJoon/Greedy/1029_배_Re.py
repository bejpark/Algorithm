"""
#1092
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다.
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다.
셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다.
넷째 줄에는 각 박스의 무게가 주어진다.
이 값도 1,000,000보다 작거나 같은 자연수이다.

#출력
첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다.
만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.
"""

"""
#1 첫 시도 시간초과
#2 두 번째 시도 오답( 반례 : 2 / 1 2 / 4 / 1 1 2 2)
import sys
n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

count=0
if crane[0] < box[0]:
    print(-1)
    sys.exit()
index=0
while index!=m:
    for i in range(n):   
        #print('i==',i)
        if crane[i]>=box[index]:
            #print('append',box[index])
            index+=1
            #print('index plus : ',index)
        else:
            pos+=1
        if index==m:
            #print('break if index==m')
            break

    count+=1
    #print('count, after count:',count)

print(count)

"""             

#3
import sys
n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
if crane[0] < box[0]:
    print(-1)
    sys.exit()
positions=[0]*n #크레인이 옮겨야 하는 박스 번호
checked=[False]*m #박스 옮긴지 여부
result=0
count=0

while True:
    if count==len(box):
        break
    for i in range(n):
        while positions[i]<len(box):
            if not checked[positions[i]] and crane[i]>=box[positions[i]]:
                checked[positions[i]]=True
                positions[i]+=1
                count+=1
                break
            positions[i]+=1
    result+=1

print(result)

