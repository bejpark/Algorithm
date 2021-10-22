#내는,,,이거,,,못하겠다,,,

n,k=map(int,input().split())
board=[]
unit=[]
tmp_board,tmp_order=[],[]
d=[(),(0,1),(0,-1),(-1,0),(1,0)]
for _ in range(n):
    board.append(list(map(int,input().split())))
for _ in range(k):
    unit.append(list(map(int,input().split())))

tmp_board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(k):  # 최초로 채움
    x, y, directions = unit[i]
    tmp_board[x][y].append((i, directions))

while True:

    for i in range(k): #각 말들 이동
        x, y, directions = unit[i]
        X=x+d[directions][0]
        Y=y+d[directions][1]
        if 0<=X<n and 0<=Y<n:
            info=(i,directions) #기본적인 정보
            if len(tmp_board[x][y])>2: #2개이상 겹쳐져있다면
                for ii in len(tmp_board[x][y]):
                    if tmp_board[x][y][0]==i: #그 위의것들 이동
                        info=tmp_board[x][y][ii:]
                        tmp_board[x][y]=tmp_board[x][y][:ii]
                        break
            if board[X][Y]!=2:
                tmp_board[X][Y].extend(info)
                unit[i] = (X, Y, directions)  # 말이 있는 곳
                if board[X][Y]==1:
                    tmp_board[X][Y]=tmp_board[X][Y].reverse()
                    print(X,Y,'위치에 1 발견, 그자리 리버스')
                    print(tmp_board[X][Y])

            else:
                if directions == 1: new_dir = 2  # 방향 반대로 바꾸기 (식으로 표현을 못하겠어서 일일히 만듬)
                elif directions == 2: new_dir = 1
                elif directions == 3: new_dir = 4
                else: new_dir = 3
                XX,YY=x+d[new_dir][0],y+d[new_dir][1]
                info[0]=(i,new_dir)
                if board[XX][YY]==2: #튕긴쪽도 파란색이라면
                    tmp_board[x][y].extend(info)
                    unit[i] = (x, y, new_dir)
                elif 0<=XX<n and 0<=YY<n: #반대로 튕길 수 있으면
                    tmp_board[XX][YY].extend(info)
                    unit[i]=(XX,YY,new_dir)
                else: #튕긴쪽 막혀있으면
                    tmp_board[x][y].extend(info)
                    unit[i]=(x,y,new_dir)



