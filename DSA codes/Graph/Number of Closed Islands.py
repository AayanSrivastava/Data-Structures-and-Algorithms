from collections import deque
class Solution:
    def bfs(self,row,col,vis,matrix):
        n,m=len(matrix),len(matrix[0])
        q=deque([[row,col]])
        vis[row][col]=1
        l=[[-1,0],[0,-1],[1,0],[0,1]]
        while q:
            row,col=q.popleft()
            matrix[row][col]=0
            for i,j in l:
                nrow=row+i
                ncol=col+j
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and matrix[nrow][ncol]==1 and vis[nrow][ncol]==0):
                    q.append([nrow,ncol])
                    vis[nrow][ncol]=1
                    
        def closedIslands(self, matrix, N, M):
            vis=[[0]*M for i in range(N)]
            self.ans=0
            for i in range(N):
                for j in range(M):
                    if i==0 or j==0 or i==N-1 or j==M-1:
                        if matrix[i][j]==1 and vis[i][j]==0:
                            self.bfs(i,j,vis,matrix)
                            
            vis=[[0]*M for i in range(N)]
            for i in range(N):
                for j in range(M):
                    if matrix[i][j]==1 and vis[i][j]==0:
                        self.ans+=1
                        self.bfs(i,j,vis,matrix)
            return self.ans