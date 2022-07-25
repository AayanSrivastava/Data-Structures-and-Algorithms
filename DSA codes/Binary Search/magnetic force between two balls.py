class Solution:
    def isvalid(self,A,N,M,mx):
        place=1
        prev=A[0]
        for i in range(1,N):
            if A[i]-prev>=mx:
                place+=1
                prev=A[i]
                if place==M:
                    return True
        if place<M:
            return False
        return True
        
    def maxDistance(self, position,m):
        position.sort()
        N=len(position)
        if N<m:
            return N+1
        start=0
        end=position[N-1]
        res=0
        while start<=end:
            mid=start+(end-start)//2
            if self.isvalid(position,N,m,mid)==True:
                res=mid
                start=mid+1
            else:
                end=mid-1
        return res