class Solution:
    m,n = 0,0
    flag=False
    visited=[]
    def exist(self, board: List[List[str]], word: str) -> bool:
        global m,n,flag, visited
        m,n=len(board),len(board[0])
        flag=False
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]: #시작점 찾기, 시작할 때 visited 초기화하고 시작해야함
                    visited=[[False]*n for _ in range(m)]
                    visited[i][j]=True #시작점을 방문하고 시작
                    Solution.graph_search(i,j,board,word,1)
        return flag

    def graph_search(x,y,board,word,idx): #DFS
            global m,n,flag, visited
            if idx==len(word): #제일 마지막까지 순회했다면
                flag=True
                #print('found')
                return
            d = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in d:
                X,Y=x+dx,y+dy
                if 0<=X<m and 0<=Y<n and not visited[X][Y]:
                    if board[X][Y]==word[idx]:
                        #print(X,Y,board[X][Y])
                        visited[X][Y]=True
                        Solution.graph_search(X,Y,board,word,idx+1)
                        visited[X][Y]=False


                    
                
        
