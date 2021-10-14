import sys
def move(order):
    global bucket,cloud
    od, level = order
    d=[(0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    #order 는 1부터이므로 앞에 빈칸만듬
    dx,dy = d[od]
    new_cloud=[]
    for x,y in cloud: #구름 이동 후 점수
        X=(x+dx*level)%n
        Y=(y+dy*level)%n
        new_cloud.append((X,Y))
        bucket[X][Y]+=1
        #print(X,Y,"자리에 +1 = ",bucket[X][Y])
    
    
    for x,y in new_cloud: #물이 온 자리에서 대각선 탐색
        for i in range(2,9,2):
            dx,dy=d[i]
            X=x+dx
            Y=y+dy
            if 0<=X<n and 0<=Y<n:
                if bucket[X][Y]!=0:
                    #print(dx,dy,'만큼',x,y,'에 +1')
                    bucket[x][y]+=1
    
    cloud=[]
    for i in range(n): #새로운 클라우드 갱신
        for j in range(n):
            if (i,j) not in new_cloud:
                if bucket[i][j]>=2:
                    cloud.append((i,j))
                    bucket[i][j]-=2
                    #print(i,j,'클라우드추가')

            


n,m = map(int,sys.stdin.readline().split())
bucket=[]
orders=[]
result=0
cloud=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(n):
    bucket.append(list(map(int,sys.stdin.readline().split())))

for _ in range(m):
    orders.append(list(map(int,sys.stdin.readline().split())))


for order in orders:
    move(order)

for lst in bucket:
    result+=sum(lst)
print(result)
