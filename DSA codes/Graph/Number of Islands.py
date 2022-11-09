import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def bfs(self,row,col,vis,grid):
        vis[row][col]=1
        q=deque([[row,col]])
        n=len(grid)
        m=len(grid[0])
        while q:
            row,col=q.pop()
            for i in range(-1,2):
                for j in range(-1,2):
                    nrow=row+i
                    ncol=col+j
                    if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and not vis[nrow][ncol]):
                        vis[nrow][ncol]=1
                        q.append([nrow,ncol])
                    
    def numIslands(self,grid):
        n=len(grid)
        m=len(grid[0])
        cnt=0
        vis=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j]:
                    cnt+=1
                    self.bfs(i,j,vis,grid)
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))