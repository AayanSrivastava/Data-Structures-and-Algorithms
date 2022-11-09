from collections import deque
class Solution:
    #Function to find unit area of the largest region of 1s.
    def bfs(self,row,col,grid):
        area=1
        q=deque([[row,col]])
        n=len(grid)
        m=len(grid[0])
        l=[[-1,0],[1,0],[0,-1],[0,1],[1,-1],[1,1],[-1,-1],[-1,1]]
        while q:
            row,col=q.popleft()
            for i,j in l:
                nrow=row+i
                ncol=col+j
                if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1):
                    grid[nrow][ncol]=0
                    q.append([nrow,ncol])
                    area+=1
        return area

    def findMaxArea(self, grid):
        n=len(grid)
        m=len(grid[0])
        max_area=0
        vis=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    grid[i][j]=0
                    max_area=max(max_area,self.bfs(i,j,grid))
        return max_area

#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends