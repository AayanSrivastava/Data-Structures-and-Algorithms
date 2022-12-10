from collections import deque
class Solution:
    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        x,y=KnightPos[0]-1,KnightPos[1]-1
        t1,t2=TargetPos[0]-1,TargetPos[1]-1
        vis=[[0 for i in range(N+1)] for j in range(N+1)]
        vis[x][y]=1
        q=deque([])
        q.append((x,y))
        moves=[[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
        ans=0
        if x==t1 and y==t2:
            return ans
        while q:
            ans+=1
            n=len(q)
            for i in range(n):
                row,col=q.popleft()
                if row==t1 and col==t2:
                    return ans-1
                for i,j in moves:
                    nrow=row+i
                    ncol=col+j
                    if(nrow>=0 and nrow<N and ncol>=0 and ncol<N and vis[nrow][ncol]==0):
                        q.append((nrow,ncol))
                        vis[nrow][ncol]=1
        return ans