import heapq
class Solution:
    def minPathSum(self, grid):
        if len(grid)==1 and len(grid[0])==1:
            return grid[0][0]
        n=len(grid)
        m=len(grid[0])
        dist=[[float('inf') for i in range(m)] for j in range(n)]
        vis=[[0 for i in range(m)] for j in range(n)]
        minheap=[(grid[0][0],0,0)]
        l=[[1,0],[0,1]]
        vis[0][0]=1
        dist[0][0]=0
        
        while minheap:
            cost,row,col=heapq.heappop(minheap)
            vis[row][col]=1
            for i,j in l:
                nrow=row+i
                ncol=col+j
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and cost+grid[nrow][ncol]<dist[nrow][ncol]):
                    vis[nrow][ncol]=1
                    dist[nrow][ncol]=cost+grid[nrow][ncol]
                    heapq.heappush(minheap,(dist[nrow][ncol],nrow,ncol))
        return dist[n-1][m-1]