class Solution:
    def solve(self,x,y,m,n,visited,ans,path):

        # you have reached x,y here
        # base case
        # print(path)
        if x==n-1 and y==n-1:
            ans.append(path)
            return
        
        # now 4 choices - D,L,R,U
        visited[x][y]=1
        # down
        if (x+1<n and visited[x+1][y]==0 and m[x+1][y]==1):
            self.solve(x+1,y,m,n,visited,ans,path+'D')
        
        # left
        if (y-1>=0 and visited[x][y-1]==0 and m[x][y-1]==1):
            self.solve(x,y-1,m,n,visited,ans,path+'L')
            
        # right
        if (y+1<n and visited[x][y+1]==0 and m[x][y+1]==1):
            self.solve(x,y+1,m,n,visited,ans,path+'R')
        
        # up
        if (x-1>=0 and visited[x-1][y]==0 and m[x-1][y]==1):
            self.solve(x-1,y,m,n,visited,ans,path+'U')
        
        visited[x][y]=0

        return
    def ratmaze(self,m,n):
        ans=[]
        path=""
        visited=[[0]*n for i in range(n)]

        if m[0][0]==0:
            return ans
        self.solve(0,0,m,n,visited,ans,path)
        return ans

    
l=Solution()
m=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
n=4
ans=l.ratmaze(m,n)
for i in ans:
    print(i,end=" ")