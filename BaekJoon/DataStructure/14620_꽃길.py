"""
#14620
2017년 4월 5일 식목일을 맞이한 진아는 나무를 심는 대신 하이테크관 앞 화단에 꽃을 심어 등교할 때 마다 꽃길을 걷고 싶었다.

진아가 가진 꽃의 씨앗은 꽃을 심고나면 정확히 1년후에 꽃이 피므로 진아는 다음해 식목일 부터 꽃길을 걸을 수 있다.

하지만 진아에게는 꽃의 씨앗이 세개밖에 없었으므로 세 개의 꽃이 하나도 죽지 않고 1년후에 꽃잎이 만개하길 원한다.

꽃밭은 N*N의 격자 모양이고 진아는 씨앗을 (1,1)~(N,N)의 지점 중 한곳에 심을 수 있다.
꽃의 씨앗은 그림 (a)처럼 심어지며 1년 후 꽃이 피면 그림 (b)모양이 된다.

꽃을 심을 때는 주의할 점이있다. 어떤 씨앗이 꽃이 핀 뒤 다른 꽃잎(혹은 꽃술)과 닿게 될 경우 두 꽃 모두 죽어버린다.
또 화단 밖으로 꽃잎이 나가게 된다면 그 꽃은 죽어버리고 만다.

그림(c)는 세 꽃이 정상적으로 핀 모양이고 그림(d)는 두 꽃이 죽어버린 모양이다.

하이테크 앞 화단의 대여 가격은 격자의 한 점마다 다르기 때문에 진아는 서로 다른 세 씨앗을 모두 꽃이 피게하면서 가장 싼 가격에 화단을 대여하고 싶다.

단 화단을 대여할 때는 꽃잎이 핀 모양을 기준으로 대여를 해야하므로 꽃 하나당 5평의 땅을 대여해야만 한다.

돈이 많지 않은 진아를 위하여 진아가 꽃을 심기 위해 필요한 최소비용을 구해주자!

#입력
입력의 첫째 줄에 화단의 한 변의 길이 N(6≤N≤10)이 들어온다.

이후 N개의 줄에 N개씩 화단의 지점당 가격(0≤G≤200)이 주어진다.

#출력
꽃을 심기 위한 최소 비용을 출력한다.
"""

#1 오답 -> 테두리 한칸 안쪽의 조합좌표 구성, 좌표의 거리가 3이하인 경우 겹침
from itertools import combinations
def can_plant3(a,b,c):
    can = True
    ab_dis = abs(a[0]-b[0]) +abs(a[1]-b[1])
    ac_dis = abs(a[0]-c[0]) +abs(a[1]-c[1])
    bc_dis = abs(c[0]-b[0]) +abs(c[1]-b[1])
    if ab_dis<3 or ac_dis<3 or bc_dis<3:
        can = False
    return can
             

n = int(input())
garden = []
price = 99999999
d = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(n):
    garden.append(list(map(int,input().split())))
#print(garden)


idx = []
for i in range(n-2):
    for j in range(n-2):
        idx.append((i+1,1+j))
idx_c = list(combinations(idx,3))
#print(idx_c)
#print(idx_c)
count=0
for a,b,c in idx_c:
    if can_plant3(a,b,c):
        count+=1
        cost = 0
        for x,y in (a,b,c):
            for dx, dy in d:
                cost += garden[x+dx][y+dy]
            cost += garden[x][y]
        #print(cost)
        if cost< price:
            price = cost
print(price)

"""
#2
N = int(input())
G = [list(map(int,input().split())) for i in range(N)]

ans = 10000
dx, dy = [0,0,0,1,-1],[0,1,-1,0,0]
def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower//N
        y = flower%N
        if x==0 or x==N-1 or y==0 or y==N-1:
            return 10000
        
        for w in range(5):
            flow.append((x+dx[w],y+dy[w])) 
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) !=15:
        return 10000
    return ret


for i in range(N*N):
    for j in range(i+1,N*N):
        for k in range(j+1,N*N):
            ans = min(ans,ck([i,j,k]))

print(ans)
"""
