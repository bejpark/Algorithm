class Solution:
    visited=list()
    n,m=0,0
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt=0
        global n,m
        n=len(board)
        m=len(board[0])
        
        global visited
        visited = [[False]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=='X' and not visited[i][j]:
                    cnt+=1
                    visited[i][j]=True
                    #print(i,j)
                    Solution.search(board,i,j)
        print(visited)

        # X.X.X
        # .X.X.
        # .X...
        # .X..X
        # .X...
        # X.XXX
        # .X...
        # .X.X.
        # X.X.X
        # .X..X
        return cnt
    
    def search(board,x,y):
        global visited,m,n
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        direction=[]
        for dx,dy in d:
            X,Y=x+dx,y+dy
            if 0<=X<n and 0<=Y<m:
                if board[X][Y]=='X':
                    visited[X][Y]=True
                    direction=[X,Y,dx,dy] #방향은 한방향임
                    
        while direction: #direction이 갱신되면 들어옴
            X=direction[0]+direction[2]
            Y=direction[1]+direction[3]
            if 0<=X<n and 0<=Y<m:
                if board[X][Y]=='X':
                    visited[X][Y]=True
                    direction[0]=X
                    direction[1]=Y
                else:
                    break
            else: #넘어가면 break
                break
            
            
        
