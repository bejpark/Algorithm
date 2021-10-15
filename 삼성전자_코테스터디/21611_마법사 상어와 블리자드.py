N,M = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
order=[list(map(int,input().split())) for _ in range(M)]



def rotate(x,y,direction,l):
    next_dir=(direction+1)%4
    if 0<=x<N and 0<=y<N:
        if direction==0:
            for i in range(l):
                print(x+i,y,' = ',board[x+i][y])
            rotate(x+l,y,next_dir,l+1)
        elif direction==1:
            for i in range(l):
                print(x,y+i,' = ',board[x][y+i])
            rotate(x,y+l,next_dir,l)
        elif direction==2:
            for i in range(l):
                print(x-i,y,' = ',board[x-i][y])
            rotate(x-l,y,next_dir,l)
        else:
            for i in range(l+1):
                print(x,y-i,' = ',board[x][y-i])
            rotate(x,y-l-1,next_dir,l+1)

print(board[N//2][N//2])
rotate(N//2,N//2-1,0,1)
