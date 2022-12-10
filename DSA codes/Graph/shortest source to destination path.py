from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        if A[0][0]==0 or A[X][Y]==0:
            return -1
        l=[[-1,0],[0,-1],[1,0],[0,1]]
        vis=[[0 for i in range(M)] for j in range(N)]
        vis[0][0]=1
        q=deque([])
        q.append((0,0))
        ans=0
        while q:
            ans+=1
            n=len(q)
            for i in range(n):
                row,col=q.popleft()
                if row==X and col==Y:
                    return ans-1
                for i,j in l:
                    nrow=row+i
                    ncol=col+j
                    if(nrow>=0 and nrow<N and ncol>=0 and ncol<M and A[nrow][ncol]==1 and vis[nrow][ncol]==0):
                        q.append((nrow,ncol))
                        vis[nrow][ncol]=1
        return -1